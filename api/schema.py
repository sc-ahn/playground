from pydantic import BaseModel, Field


class SchoolInfo(BaseModel):
    district_code: str = Field(
        ..., title="시도교육청코드", description="시도교육청코드"
    )
    district_name: str = Field(..., title="시도교육청명", description="시도교육청명")
    standard_code: str = Field(..., title="행정표준코드", description="행정표준코드")
    school_name: str = Field(..., title="학교명", description="학교명")
    school_name_eng: str = Field(..., title="학교명(영문)", description="학교명(영문)")
    school_type: str = Field(..., title="학교종류", description="학교종류")
    city: str = Field(..., title="시도", description="시도")
    org_name: str = Field(..., title="관할조직명", description="관할조직명")
    init_type: str = Field(..., title="설립구분", description="설립구분")
    street_name_zip: str = Field(
        ..., title="도로명우편번호", description="도로명우편번호"
    )
    street_name_addr: str = Field(..., title="도로명주소", description="도로명주소")
    street_name_addr_detail: str = Field(
        ..., title="도로명주소상세", description="도로명주소상세"
    )
    phone: str = Field(..., title="전화번호", description="전화번호")
    homepage: str = Field(..., title="홈페이지주소", description="홈페이지주소")
    coeducation: str = Field(..., title="남녀공학구분", description="남녀공학구분")
    fax: str = Field(..., title="팩스번호", description="팩스번호")
    highschool_type: str = Field(..., title="고등학교유형", description="고등학교유형")
    special_industry_class_exist: str = Field(
        ..., title="산업체특별학급존재여부", description="산업체특별학급존재여부"
    )
    highschool_generalist: str = Field(
        ..., title="고등학교일반전문구분명", description="고등학교일반전문구분명"
    )
    special_purpose_highschool_affiliation_name: str = Field(
        ..., title="특수목적고등학교계열명", description="특수목적고등학교계열명"
    )
    post_admission_organization_clarification: str = Field(
        ..., title="입시전후기구분명", description="입시전후기구분명"
    )
    day_or_night: str = Field(..., title="주야구분명", description="주야구분명")
    establishment_date: str = Field(..., title="설립일자", description="설립일자")
    opening_date: str = Field(..., title="개교기념일", description="개교기념일")
    updated_at_date: str = Field(
        ..., title="데이터기준일자", description="데이터기준일자"
    )


class EssentialSchoolInfo(BaseModel):
    school_name: str = Field(..., title="학교명", description="학교명")
    standard_code: str = Field(..., title="행정표준코드", description="행정표준코드")
    district_code: str = Field(
        ..., title="시도교육청코드", description="시도교육청코드"
    )


class ScheduleInfo(BaseModel):
    ATPT_OFCDC_SC_CODE: str = Field(
        ...,
    )
    SD_SCHUL_CODE: str = Field(
        ...,
    )
    AY: str = Field(
        ...,
    )
    AA_YMD: str = Field(
        ...,
    )
    ATPT_OFCDC_SC_NM: str = Field(
        ...,
    )
    SCHUL_NM: str = Field(
        ...,
    )
    DGHT_CRSE_SC_NM: str = Field(
        ...,
    )
    SCHUL_CRSE_SC_NM: str = Field(
        ...,
    )
    EVENT_NM: str = Field(
        ...,
    )
    EVENT_CNTNT: str = Field(
        ...,
    )
    ONE_GRADE_EVENT_YN: str = Field(
        ...,
    )
    TW_GRADE_EVENT_YN: str = Field(
        ...,
    )
    THREE_GRADE_EVENT_YN: str = Field(
        ...,
    )
    FR_GRADE_EVENT_YN: str = Field(
        ...,
    )
    FIV_GRADE_EVENT_YN: str = Field(
        ...,
    )
    SIX_GRADE_EVENT_YN: str = Field(
        ...,
    )
    SBTR_DD_SC_NM: str = Field(
        ...,
    )
    LOAD_DTM: str = Field(
        ...,
    )


class ScheduleSummary(BaseModel):
    midterm_exam_begin: str = Field(
        ...,
    )
    midterm_exam_end: str = Field(
        ...,
    )
    final_exam_begin: str = Field(
        ...,
    )
    final_exam_end: str = Field(
        ...,
    )
    winter_vacation_begin: str = Field(
        ...,
    )
    winter_vacation_end: str = Field(
        ...,
    )
    spring_vacation_begin: str = Field(
        ...,
    )
    spring_vacation_end: str = Field(
        ...,
    )
    summer_vacation_begin: str = Field(
        ...,
    )
    summer_vacation_end: str = Field(
        ...,
    )
