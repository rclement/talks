from typing import Dict, List

from .celery import celery_app


def get_all() -> List[Dict[str, str]]:
    return [
        {"name": "John Doe", "email": "john@doe.com"},
        {"name": "Jane Doe", "email": "jane@doe.com"},
    ]


celery_app.task(get_all, name="users.get_all", ignore_result=False)
