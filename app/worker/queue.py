import json
import os

import redis
from redis.exceptions import RedisError

REDIS_URL = os.getenv("REDIS_URL")
if not REDIS_URL:
    raise RuntimeError("REDIS_URL environment variable is required")

QUEUE_NAME = os.getenv("QUEUE_NAME", "tasks")

redis_client = redis.from_url(
    REDIS_URL,
    decode_responses=True,
)


def publish_task(task_id: int) -> None:
    """
    Publica task na fila Redis.
    Não quebra a aplicação se Redis estiver indisponível.
    """
    message = json.dumps({"task_id": task_id})

    try:
        redis_client.rpush(QUEUE_NAME, message)
    except RedisError as e:
        print(f"[Redis Publish Error] {e}")
