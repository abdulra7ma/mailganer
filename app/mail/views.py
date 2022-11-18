# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import MailRecipientCreateForm, NewsletterForm, ScheduledMailForm
from .tasks import broadcast_newsletter, broadcast_scheduled_newsletter


class SubscribeView(FormView):
    template_name = 'letter/index.html'
    form_class = MailRecipientCreateForm
    success_url = reverse_lazy("subscribe")

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())


class NewsletterView(FormView):
    template_name = 'letter/newsletter.html'
    form_class = NewsletterForm
    success_url = reverse_lazy("newsletter")

    def form_valid(self, form):
        form.save()
        broadcast_newsletter.delay(form.instance.id)
        return HttpResponseRedirect(self.get_success_url())


class ScheduledMailView(FormView):
    template_name = 'letter/newsletter.html'
    form_class = ScheduledMailForm
    success_url = reverse_lazy("scheduled-newsletter")

    def form_valid(self, form):
        form.save()
        instance = form.instance
        broadcast_scheduled_newsletter.apply_async((form.instance.id,), eta=instance.send_on)
        return HttpResponseRedirect(self.get_success_url())
