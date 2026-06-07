from pydantic import BaseModel, Field


class ProjectCreate(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    description: str = Field(default="", max_length=200)


class Project(ProjectCreate):
    id: int