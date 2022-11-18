from django.conf import settings
from django.core.mail import send_mass_mail
from django.template.loader import render_to_string

from mail.selectors.recipient import get_all_recipient
from django.core.mail import get_connection, EmailMultiAlternatives


def send_mass_html_mail(datatuple, fail_silently=False):
    """
    Given a datatuple of (subject, text_content, html_content, from_email,
    recipient_list), sends each message to each recipient list.

    :param datatuple:
    :param fail_silently:
    :return: number of emails sent
    """
    messages = []
    connection = get_connection(fail_silently=fail_silently)
    for subject, text, html, from_email, recipient in datatuple:
        message = EmailMultiAlternatives(subject, text, from_email, recipient)
        message.attach_alternative(html, 'text/html')
        messages.append(message)
    return connection.send_messages(messages)


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
            messages.append((newsletter.title, message, message, settings.EMAIL_FROM, [recipient.mail_address]))
        return tuple(messages)

    def send_emails(self, newsletter):
        messages = self.pre_recipients_messages(newsletter)
        send_mass_html_mail(messages, fail_silently=False)
        return True
