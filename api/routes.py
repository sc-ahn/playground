import logging
from collections import defaultdict
from typing import Annotated

import orjson
from aiohttp import ClientSession
from fastapi import APIRouter, BackgroundTasks, Path, Query
from fastapi.responses import ORJSONResponse

from api.db.mongo import db
from api.enums import SchoolType
from api.responses import GetSchoolResponseOkay
from api.schema import ScheduleInfo, SchoolInfo
from api.services import get_org_list
from api.services import get_school_list as get_school_list_from_db
from api.settings import env
from api.tasks.csv_reformer import get_file_info

router = APIRouter(tags=["학사일정"])


def is_target_event(event_name):
    return any(
        keyword in event_name
        for keyword in [
            "방학",
            "개학",
            "졸업",
            "종업",
            "입학",
            "중간",
            "기말",
        ]
    )


@router.patch("/metadata")
async def patch_school_metadata(background_tasks: BackgroundTasks) -> ORJSONResponse:
    """
    학교 메타데이터를 업데이트하는 백그라운드 작업을 생성합니다.
    """
    background_tasks.add_task(get_file_info)
    return ORJSONResponse(
        status_code=200,
        content={
            "status": True,
            "message": "메타데이터 초기화를 진행합니다.",
        },
    )


@router.get("/org")
async def get_org_name(
    except_closed: Annotated[
        bool,
        Query(
            title="폐지된 조직명 제외 여부",
            description="폐지된 조직명을 제외할지 여부",
            json_schema_extra={"example": True},
        ),
    ] = True,
) -> ORJSONResponse:
    """
    학교의 관할 조직명을 가져옵니다.
    폐지된 조직명은 제외합니다.
    """
    org_name_list = await get_org_list(db, except_closed)
    return ORJSONResponse(
        status_code=200,
        content={
            "status": True,
            "org_name": org_name_list,
        },
    )


@router.get(
    "/서울/{school_type}",
    status_code=200,
    responses={
        200: {
            "model": GetSchoolResponseOkay,
        }
    },
)
async def get_school_list(
    school_type: Annotated[
        SchoolType,
        Path(
            title="학교종류",
            description="학교종류",
            json_schema_extra={"example": "중학교"},
        ),
    ],
    limit: Annotated[
        int,
        Query(
            title="한 페이지에 보여질 학교 수",
            description="페이지네이션을 위한 옵션입니다.",
            json_schema_extra={"example": 10},
        ),
    ] = 10,
    page: Annotated[
        int,
        Query(
            title="페이지 번호",
            description="페이지네이션을 위한 옵션입니다.",
            json_schema_extra={"example": 1},
        ),
    ] = 1,
) -> ORJSONResponse:
    school_list = await get_school_list_from_db(
        db,
        city="서울",
        school_type=school_type,
        page=page,
        limit=limit,
    )
    return {
        "status": True,
        "school_list": school_list,
    }


@router.get("/서울/{school_type}/{standard_code}/일정")
async def get_school_schedule(
    school_type: Annotated[
        SchoolType,
        Path(
            title="학교종류",
            description="학교종류",
            json_schema_extra={"example": "중학교"},
        ),
    ],
    standard_code: Annotated[
        str,
        Path(
            title="표준학교코드",
            description="표준학교코드",
            json_schema_extra={"example": "7130165"},
        ),
    ],
):
    if not env.neis_api_key:
        return ORJSONResponse(
            status_code=401,
            content={
                "status": False,
                "message": "학사일정 API를 사용하기 위해서는 NEIS API 키가 필요합니다.",
            },
        )

    generator = db.school_info.find(
        {
            "city": {"$regex": "^서울"},
            "school_type": school_type,
            "standard_code": standard_code,
        }
    )

    schedule = defaultdict(dict)

    async with ClientSession() as session:
        async for school_info in generator:
            school_info_model = SchoolInfo(**school_info)
            standard_code = school_info_model.standard_code
            district_code = school_info_model.district_code
            async with session.get(
                "https://open.neis.go.kr/hub/SchoolSchedule",
                params={
                    "Type": "json",
                    "pIndex": 1,
                    "pSize": 1000,
                    "KEY": env.neis_api_key,
                    "ATPT_OFCDC_SC_CODE": district_code,
                    "SD_SCHUL_CODE": standard_code,
                    "AA_FROM_YMD": "2024",
                    "AA_TO_YMD": "2025",
                },
            ) as response:
                try:
                    response.raise_for_status()
                except Exception:
                    logging.error(
                        "Failed to get school schedule for %s",
                        standard_code,
                    )
                    continue
                # NOTE: html로 뿌려줌..;
                raw_text = await response.text(encoding="utf-8")
                data = orjson.loads(raw_text)  # pylint: disable=no-member
                result = data.get("SchoolSchedule")
                if not result or len(result) < 2:
                    continue
                schedule_map_list = result[1].get("row", [])
                aa_ymd_by_event_nm = defaultdict(list)
                # range_by_event_nm = defaultdict(dict)
                for schedule_map in schedule_map_list:
                    schedule_info_model = ScheduleInfo(**schedule_map)
                    event_nm = schedule_info_model.EVENT_NM
                    if not is_target_event(event_nm):
                        continue
                    aa_ymd = schedule_info_model.AA_YMD
                    aa_ymd_by_event_nm[event_nm].append(aa_ymd)
                schedule = aa_ymd_by_event_nm
            break
    return ORJSONResponse(
        status_code=200,
        content={
            "status": True,
            "schedule": schedule,
        },
    )
