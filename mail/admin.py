# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ScheduledMail, Newsletter, MailRecipient


@admin.register(ScheduledMail)
class MailAdmin(admin.ModelAdmin):
    pass


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    pass


@admin.register(MailRecipient)
class RecipientAdmin(admin.ModelAdmin):
    pass
