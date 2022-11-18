from mail.models import Newsletter, ScheduledMail
from mail.services.mail.main import Mail
from celery import shared_task
from core import celery_app


@celery_app.task(bind=True)
def broadcast_newsletter(self, newsletter_id):
    """
    Send newly created newsletter to all subscribes

    :param newsletter_id: newly created Newsletter object id
    :return: Boolean
    """

    print("newsletter_id is ", newsletter_id)

    newsletter = Newsletter.objects.get(id=newsletter_id)

    mail = Mail()
    mail.send_emails(newsletter)

    return True


@celery_app.task(bind=True)
def broadcast_scheduled_newsletter(self, scd_newsletter_id):
    """
    Send newly created newsletter to all subscribes

    :param scd_newsletter_id: newly created ScheduledMail object id
    :return: Boolean
    """

    print("newsletter_id is ", ScheduledMail)

    newsletter = ScheduledMail.objects.get(id=scd_newsletter_id)

    mail = Mail()
    mail.send_emails(newsletter)

    return True