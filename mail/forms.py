from django.forms import ModelForm
from .models import MailRecipient, Newsletter


class MailRecipientCreateForm(ModelForm):
    class Meta:
        model = MailRecipient
        fields = ["mail_address", "first_name", "last_name", "birth_day"]


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'