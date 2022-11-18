# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import date


class Newsletter(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()

    def __str__(self):
        return self.title


class MailRecipient(models.Model):
    mail_address = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birth_day = models.DateField()

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.mail_address


class ScheduledMail(models.Model):
    subject = models.CharField(max_length=40)
    template = models.FileField(upload_to='mail/mails')
    send_on = models.DateTimeField(default=timezone.now())
    recipients_list = models.ManyToManyField(MailRecipient, related_name='mail_list')

    def __str__(self):
        return self.subject

    @classmethod
    def get_today_mail(cls):
        today = date.today()
        return cls.objects.filter(send_on__year=today.year, send_on__month=today.month, send_on__day=today.day)
