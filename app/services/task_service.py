from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate
from app.worker.queue import publish_task


def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    publish_task(db_task.id)

    return db_task


def list_tasks(db: Session):
    return db.query(Task).all()
