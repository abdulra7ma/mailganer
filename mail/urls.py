from django.conf.urls import url

from .views import NewsletterView, SubscribeView

urlpatterns = [
    url(r'^subscribe', SubscribeView.as_view(), name="subscribe"),
    url(r'^newsletter', NewsletterView.as_view(), name="newsletter"),
]
