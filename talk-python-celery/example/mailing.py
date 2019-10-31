from typing import Dict, List
from celery import chain, signature

from .celery import celery_app


def send_newsletter_user(user: Dict[str, str]) -> None:
    print(f"Sending newsletter to {user['name']}: {user['email']}")


def send_newsletter_all(all_users: List[Dict[str, str]]) -> None:
    for user in all_users:
        send_newsletter_user(user)


def send_newsletter() -> None:
    users_sig = signature("users.get_all", queue="users")

    newsletters_sig = signature("mailing.send_newsletter_all", queue="mailing")

    task_chain = chain(users_sig | newsletters_sig)
    task_chain.apply_async()


celery_app.task(
    send_newsletter_user, name="mailing.send_newsletter_user", ignore_result=True
)

celery_app.task(
    send_newsletter_all, name="mailing.send_newsletter_all", ignore_result=True
)

celery_app.task(send_newsletter, name="mailing.send_newsletter", ignore_result=True)
