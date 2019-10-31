from celery import schedules

from .celery import celery_app


celery_app.conf.update(
    enable_utc=True,
    timezone="UTC",
    beat_schedule={
        "send-report-every-5s": {
            "task": "tasks.send_report",
            "kwargs": {"email": "admin@domain.com"},
            "options": {"queue": "tasks"},
            "schedule": 5,
        },
        "send-newsletter-minutely": {
            "task": "mailing.send_newsletter",
            "options": {"queue": "mailing"},
            "schedule": schedules.crontab(
                minute="*",
                hour="*",
                day_of_week="*",
                day_of_month="*",
                month_of_year="*",
            ),
        },
    },
)
