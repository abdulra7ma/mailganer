from datetime import date

from django.core.management import BaseCommand

from mail.models import ScheduledMail


class Command(BaseCommand):
    help = 'Sends an email to any client for which a discount has started today.'

    def handle(self, *args, **options):
        today_mail = ScheduledMail.get_today_mail()

    for mail_message in today_mail:
        mail_message.send_scheduled_mail()
