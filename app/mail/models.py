# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.db import models
from django.utils import timezone


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
    title = models.CharField(max_length=128)
    body = models.TextField()
    send_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title + "Send it on " + str(self.send_on)
