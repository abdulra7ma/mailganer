# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import MailRecipientCreateForm, NewsletterForm
from .tasks import broadcast_newsletter


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
        broadcast_newsletter(form.instance)
        return HttpResponseRedirect(self.get_success_url())
