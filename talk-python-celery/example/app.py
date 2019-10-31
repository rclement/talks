from datetime import datetime
from celery.result import AsyncResult

from .celery import celery_app


celery_app.conf.update(
    task_routes={"tasks.*": "tasks", "users.*": "users", "mailing.*": "mailing"}
)

print("tasks.say_hi")
celery_app.send_task("tasks.say_hi", args=["Joe"])

print("tasks.talking_clock")
talking_clock_task: AsyncResult = celery_app.send_task("tasks.talking_clock")
talking_clock_task_result = AsyncResult(talking_clock_task.id, app=celery_app)
now: datetime = talking_clock_task_result.get()
print(f"result: {now}")

print("tasks.failing_task")
celery_app.send_task("tasks.failing_task")
