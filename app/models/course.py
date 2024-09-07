from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class CourseSection(BaseModel):
    course_id: Optional[int] = None
    course_name: Optional[str] = None
    uuid: Optional[str] = None
    created_at: Optional[str] = None
    course_code: Optional[str] = None
    sis_course_id: Optional[str] = None
    course_no: Optional[str] = None
    section: Optional[str] = None
    course_year: Optional[str] = None
    semester: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "course_id": 204283,
                "course_name": "COMSW4153_001_2024_3 - Cloud Computing",
                "uuid": "3jHCxUV0ck9Z8TF1sZeI8WTx47olDGkX1YPL3USM",
                "created_at": "2024-04-05T00:58:50Z",
                "course_code": "COMSW4153_001_2024_3 - Cloud Computing",
                "sis_course_id": "COMSW4153_001_2024_3",
                "course_no": "COMSW4153",
                "section": "001",
                "course_year": "2024",
                "semester": "3"
            }
        }
