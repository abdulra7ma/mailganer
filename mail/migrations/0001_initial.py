# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-18 03:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailRecipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_address', models.CharField(max_length=40)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('birth_day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=40)),
                ('template', models.FileField(upload_to='mail/mails')),
                ('send_on', models.DateTimeField(default=datetime.datetime(2022, 11, 18, 3, 7, 45, 547707, tzinfo=utc))),
                ('recipients_list', models.ManyToManyField(related_name='mail_list', to='mail.MailRecipient')),
            ],
        ),
    ]