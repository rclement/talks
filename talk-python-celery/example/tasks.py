from datetime import datetime

from .celery import celery_app


def say_hi(name: str) -> None:
    print(f"Hi, {name}!")


def talking_clock() -> datetime:
    return datetime.now()


def failing_task() -> None:
    raise RuntimeError


def send_report(email: str) -> None:
    print(f"Sending report to {email}")


celery_app.task(say_hi, name="tasks.say_hi", ignore_result=True)

celery_app.task(talking_clock, name="tasks.talking_clock", ignore_result=False)

celery_app.task(
    failing_task,
    name="tasks.failing_task",
    ignore_result=True,
    autoretry_for=(RuntimeError,),
    max_retries=5,
    retry_backoff=True,
    retry_jitter=True,
)

celery_app.task(send_report, name="tasks.send_report", ignore_result=True)
