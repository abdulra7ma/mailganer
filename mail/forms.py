from django.forms import ModelForm
from django.utils import timezone
from django import forms

from .models import MailRecipient, Newsletter, ScheduledMail

from celery import Celery


class MailRecipientCreateForm(ModelForm):
    class Meta:
        model = MailRecipient
        fields = ["mail_address", "first_name", "last_name", "birth_day"]


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'


class ScheduledMailForm(ModelForm):
    class Meta:
        model = ScheduledMail
        fields = '__all__'

    def clean(self):
        send_on = self.cleaned_data.get("send_on")

        if send_on < timezone.now():
            raise forms.ValidationError("Send On time should not be in the past")

        return super(ScheduledMailForm, self).clean()
