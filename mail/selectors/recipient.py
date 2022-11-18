from mail.models import MailRecipient


def get_all_recipient():
    """
    Query all available mail recipients and returns

    :return: All mail recipients
    """
    return MailRecipient.objects.all()
