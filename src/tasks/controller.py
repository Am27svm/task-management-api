from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException
from src.user.models import UserModel

def create_task(body: TaskSchema, db: Session,user:UserModel):
    data = body.model_dump()
    new_task = TaskModel(
        title=data["title"],
        description=data["description"],
        is_completed=data["is_completed"],
        user_id=user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def get_tasks(db: Session,user:UserModel):
    tasks = db.query(TaskModel).filter(TaskModel.user_id==user.id).all()
    return [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "is_completed": task.is_completed,
            "user_id":task.user_id,
        }
        for task in tasks
    ]


def get_one_task(id: int, db: Session,user:UserModel):
    task = db.get(TaskModel, id)
    if not task:
        raise HTTPException(404, detail="Task id not found")
    if task.user_id!= user.id:
        raise HTTPException(404, detail="Task not found")
    
    return task


def update_task(body, id: int, db: Session,user:UserModel):
    task = db.get(TaskModel, id)
    if not task:
        raise HTTPException(404, detail="Task id not found")
    if task.user_id!= user.id:
        raise HTTPException(404, detail="Task not found")
    body = body.model_dump()
    for field, value in body.items():
        if value != None:
            setattr(task, field, value)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def delete_task(id: int, db: Session,user:UserModel):
    
    task = db.get(TaskModel, id)
    
    if not task:
        raise HTTPException(404, detail="Task id not found")
    if task.user_id != user.id:
        raise HTTPException(404, detail="Task not found")
    db.delete(task)
    db.commit()

    return None


