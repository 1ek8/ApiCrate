from fastapi import APIRouter, HTTPException
from app.models import ProjectCreate, Project

router = APIRouter(prefix="/projects", tags=["projects"])

PROJECTS: list[Project] = []


@router.get("")
def list_projects():
    return PROJECTS


@router.post("", response_model=Project, status_code=201)
def create_project(payload: ProjectCreate):
    normalized_name = payload.name.strip()

    if any(project.name.lower() == normalized_name.lower() for project in PROJECTS):
        raise HTTPException(status_code=400, detail="Project with this name already exists")

    project = Project(
        id=len(PROJECTS) + 1,
        name=normalized_name,
        description=payload.description.strip()
    )
    PROJECTS.append(project)
    return project