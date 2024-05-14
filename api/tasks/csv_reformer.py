import asyncio

from api.db.mongo import db
from api.schema import SchoolInfo
from api.settings import BASE_PATH


async def get_file_info():
    with open(
        BASE_PATH / "tasks" / "school_2024_01_31.csv",
        "r",
        encoding="cp949",
    ) as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if i == 0:
                continue
            line = line.split(",")
            school_info = SchoolInfo(
                district_code=line[0],
                district_name=line[1],
                standard_code=line[2],
                school_name=line[3],
                school_name_eng=line[4],
                school_type=line[5],
                city=line[6],
                org_name=line[7],
                init_type=line[8],
                street_name_zip=line[9],
                street_name_addr=line[10],
                street_name_addr_detail=line[11],
                phone=line[12],
                homepage=line[13],
                coeducation=line[14],
                fax=line[15],
                highschool_type=line[16],
                special_industry_class_exist=line[17],
                highschool_generalist=line[18],
                special_purpose_highschool_affiliation_name=line[19],
                post_admission_organization_clarification=line[20],
                day_or_night=line[21],
                establishment_date=line[22],
                opening_date=line[23],
                updated_at_date=line[24].strip(),
            )
            await db.school_info.update_one(
                {"standard_code": line[2]},
                {"$set": school_info.model_dump()},
                upsert=True,
            )


if __name__ == "__main__":
    asyncio.run(get_file_info())
