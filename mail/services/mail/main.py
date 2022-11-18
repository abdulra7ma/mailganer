from mail.selectors.recipient import get_all_recipient
from django.template.loader import render_to_string

from django.conf import settings

from django.core.mail import send_mass_mail


class Mail:
    @staticmethod
    def pre_recipients_messages(newsletter):
        messages = []
        recipients = get_all_recipient()

        for recipient in recipients:
            message = render_to_string("email_templates/index.html", context={
                "first_name": recipient.first_name,
                "last_name": recipient.first_name,
                "message_body": newsletter.body,
            })
            messages.append((newsletter.title, message, settings.EMAIL_HOST_USER, [recipient.mail_address]))

        return tuple(recipients)

    def send_emails(self, newsletter):
        messages = self.pre_recipients_messages(newsletter)
        send_mass_mail(messages, fail_silently=False)
        return True