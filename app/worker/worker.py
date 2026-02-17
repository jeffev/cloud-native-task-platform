import json
import os
import time

import redis
from redis.exceptions import RedisError
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.task import Task

REDIS_URL = os.getenv("REDIS_URL")
if not REDIS_URL:
    raise RuntimeError("REDIS_URL environment variable is required")

QUEUE_NAME = os.getenv("QUEUE_NAME", "tasks")
PROCESSING_TIME = int(os.getenv("PROCESSING_TIME", "5"))


def create_redis_client():
    while True:
        try:
            client = redis.from_url(
                REDIS_URL,
                decode_responses=True,
            )
            client.ping()
            print("Connected to Redis")
            return client
        except RedisError:
            print("Waiting for Redis...")
            time.sleep(2)


redis_client = create_redis_client()


def process_task(task_id: int) -> None:
    db: Session = SessionLocal()
    task = None

    try:
        task = db.query(Task).filter(Task.id == task_id).first()

        if not task:
            return

        if task.status != "pending":
            return

        task.status = "processing"
        db.commit()

        time.sleep(PROCESSING_TIME)

        task.status = "done"
        db.commit()

    except Exception as e:
        if task:
            task.status = "failed"
            db.commit()
        print(f"[Worker Processing Error] {e}")

    finally:
        db.close()


def start_worker() -> None:
    print("Worker started. Waiting for tasks...")

    while True:
        try:
            result = redis_client.blpop(QUEUE_NAME, timeout=5)

            if result:
                _, message = result
                data = json.loads(message)
                process_task(data["task_id"])

        except RedisError as e:
            print(f"[Redis Error] {e}")
            time.sleep(2)
        except Exception as e:
            print(f"[Worker Error] {e}")
            time.sleep(2)


if __name__ == "__main__":
    start_worker()
