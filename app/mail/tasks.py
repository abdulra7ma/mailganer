from app.mail.models import Newsletter, ScheduledMail
from app.mail.services.mail.main import Mail
from app.core import celery_app


@celery_app.task(bind=True)
def broadcast_newsletter(self, newsletter_id):
    """
    Send newly created newsletter to all subscribes

    :param newsletter_id: newly created Newsletter object id
    :return: Boolean
    """

    newsletter = Newsletter.objects.using("default").get(id=newsletter_id)

    print("", newsletter.title)

    mail = Mail()
    mail.send_emails(newsletter)

    return True


@celery_app.task(bind=True)
def broadcast_scheduled_newsletter(self, scd_newsletter_id):
    """
    Send timed newsletter to all subscribes

    :param scd_newsletter_id: newly created ScheduledMail object id
    :return: Boolean
    """

    newsletter = ScheduledMail.objects.using("default").get(id=scd_newsletter_id)

    mail = Mail()
    mail.send_emails(newsletter)

    return True