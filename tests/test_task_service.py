from app.schemas.task import TaskCreate
from app.services.task_service import create_task


def test_create_task_service(db):

    task_data = TaskCreate(title="Service Task", description="Testing service")

    task = create_task(db, task_data)

    assert task.id == 1
    assert task.status == "pending"
