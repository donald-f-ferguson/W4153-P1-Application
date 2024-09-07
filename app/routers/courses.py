from fastapi import APIRouter

from app.models.course import CourseSection
from app.resources.course_resource import CourseResource
from app.services.service_factory import ServiceFactory

router = APIRouter()


@router.get("/courses_sections/{course_id}", tags=["users"])
async def get_courses(course_id: str) -> CourseSection:

    # TODO Do lifecycle management for singleton resource
    res = ServiceFactory.get_service("CourseResource")
    result = res.get_by_key(course_id)
    return result

