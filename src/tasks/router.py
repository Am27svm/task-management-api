from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskUpdateSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.utils.helper import is_authenticated
from src.user.models import UserModel

task_routes = APIRouter(prefix="/tasks")


@task_routes.post("/create", status_code=status.HTTP_201_CREATED)
def cerate_task(
    body: TaskSchema, db=Depends(get_db), user: UserModel = Depends(is_authenticated)
):
    return controller.create_task(body, db,user)


@task_routes.get("/all_tasks", status_code=status.HTTP_200_OK)
def get_all_tasks(
    db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)
):
    return controller.get_tasks(db,user)


@task_routes.get("/{id}", status_code=status.HTTP_200_OK)
def get_one_task(
    id: int, db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)
):
    return controller.get_one_task(id, db,user)


@task_routes.put("/update_task/{id}", status_code=status.HTTP_200_OK)
def update_one(
    body: TaskUpdateSchema,
    id: int,
    db: Session = Depends(get_db),
    user: UserModel = Depends(is_authenticated),
):
    return controller.update_task(body, id, db,user)


@task_routes.delete("/delete_task/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    id: int, db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)
):
    return controller.delete_task(id, db,user)
