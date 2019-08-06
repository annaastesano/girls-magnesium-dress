from django.conf.urls import url
from public import views

urlpatterns = [
    url(r'^$', views.index_static, name="index"),
    url(r'^createsurvey/$', views.registration, name="registration"),
    url(r'^reports/$', views.reports_admin, name="reports"),
    url(r'^reports/export$', views.generate_spreadsheet_export, name="reports_export"),
    url(r'^reports/(?P<sid>[\w]+)/$', views.report_static, name="report"),
    url(r'^reports/internal/(?P<sid>[\w]+)/$', views.internal_report, name="report-internal"),
    url(r'^reports/result/(?P<response_id>[\w]+)/$', views.report_result_static, name="report_result"),
    url(r'^result-detail/(?P<response_id>[\w]+)/$', views.result_detail, name="result-detail"),
    url(r'^thank-you/$', views.thank_you, name="thank-you"),
]
