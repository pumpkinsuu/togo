from typing import List
from pydantic import BaseModel
from datetime import date


class TaskBase(BaseModel):
    name: str
    user_id: int


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    create_date: date

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    limit: int
    tasks: List[Task] = []

    class Config:
        orm_mode = True
