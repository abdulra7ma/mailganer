from mail.services.mail.main import Mail, send_mass_html_mail


def broadcast_newsletter(newsletter):
    """
    Send newly created newsletter to all subscribes

    :param newsletter: newly created Newsletter object
    :return: Boolean
    """

    mail = Mail()
    mail.send_emails(newsletter)

    return True
