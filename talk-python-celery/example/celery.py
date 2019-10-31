import os

from typing import Optional
from celery import Celery


celery_broker_url: Optional[str] = os.environ.get("CELERY_BROKER_URL")
celery_result_backend: Optional[str] = os.environ.get("CELERY_RESULT_BACKEND")

celery_app: Celery = Celery("example")

celery_app.conf.update(
    broker_url=celery_broker_url, result_backend=celery_result_backend
)
