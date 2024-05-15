from typing import Annotated

from pydantic import BaseModel, Field

from api.schema import EssentialSchoolInfo


class GetSchoolResponseOkay(BaseModel):
    status: Annotated[
        bool,
        Field(
            description="응답 상태",
            json_schema_extra={
                "example": True,
            },
        ),
    ]
    school_list: Annotated[
        list[EssentialSchoolInfo],
        Field(
            description="학교 리스트",
            json_schema_extra={
                "example": [
                    EssentialSchoolInfo(
                        school_name="학교명",
                        standard_code="행정표준코드",
                        district_code="시도교육청코드",
                    )
                ]
            },
        ),
    ]
