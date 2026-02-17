from sqlalchemy.orm import Session

from app.models.task import Task
from app.observability.metrics import (
    TASKS_CREATED_TOTAL,
    TASKS_IN_PROGRESS,
)
from app.schemas.task import TaskCreate
from app.worker.queue import publish_task


def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.model_dump())

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    # Business metrics
    TASKS_CREATED_TOTAL.inc()
    TASKS_IN_PROGRESS.inc()

    # Publish async processing
    publish_task(db_task.id)

    return db_task


def list_tasks(db: Session):
    return db.query(Task).all()
