from async_lru import alru_cache

from api.enums import SchoolType
from api.schema import EssentialSchoolInfo


@alru_cache
async def get_org_list(db, except_closed: bool = True) -> list[str]:
    org_name_list_ = await db.school_info.distinct("org_name")
    org_name_list = [
        org_name
        for org_name in org_name_list_
        if except_closed and "폐지" not in org_name
    ]
    return org_name_list


@alru_cache(maxsize=32)
async def get_school_list(
    db,
    city: str,
    school_type: SchoolType,
    page: int = 1,
    limit: int = 10,
) -> list[EssentialSchoolInfo]:
    # city must be startswith "서울" and school_type must be equal to school_type
    query = {
        "city": {"$regex": f"^{city}"},
        "school_type": school_type,
    }
    generator = db.school_info.find(query).skip((page - 1) * limit).limit(limit)
    standard_code_list = [
        EssentialSchoolInfo(**school_info) async for school_info in generator
    ]
    return standard_code_list
