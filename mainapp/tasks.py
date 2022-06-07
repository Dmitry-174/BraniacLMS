import logging
from typing import Dict, Union

from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


@shared_task
def send_feedback_mail(message_form: Dict[str, Union[int, str]]) -> None:
    logger.info(f"Send message: '{message_form}'")
    model_user = get_user_model()
    user_obj = model_user.objects.get(pk=message_form["user_id"])
    message = message_form["message"]
    send_mail(
        "TechSupport Help",  # subject (title)
        f"message: {message} \nfrom user: {user_obj.email}",  # message
        settings.EMAIL_HOST_USER,  # send from
        ["dmitry.valiev174@gmail.com"],  # send to
        fail_silently=False,
    )
    return None
