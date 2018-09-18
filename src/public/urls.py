from django.conf import settings
from django.conf.urls import url
from django.views.generic import TemplateView
from public.views import reports_admin, registration

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="public/index.html"), name="index"),
    url(r'^createsurvey$', registration, name="registration"),
    url(r'^reports$', reports_admin, name="reports"),
    url(r'^reports/(?P<sid>[\w]+)$', TemplateView.as_view(template_name="public/report-static.html"), name="report"),
]
