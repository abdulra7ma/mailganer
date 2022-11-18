from django.conf.urls import url

from .views import NewsletterView, SubscribeView, ScheduledMailView

urlpatterns = [
    url(r'^subscribe', SubscribeView.as_view(), name="subscribe"),
    url(r'^newsletter', NewsletterView.as_view(), name="newsletter"),
    url(r'^scheduled-newsletter', ScheduledMailView.as_view(), name="scheduled-newsletter"),
]
