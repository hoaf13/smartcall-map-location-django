from django.urls import path

from report.models import Report
from .views import ReportAPI

urlpatterns = [
    path('get_all_reports/',ReportAPI.as_view(),name='get-all-report-api'),
    path('get_report_by_conversation_id/<str:conversation_id>/', ReportAPI.as_view(), name='get-report-by-conversation-id-api'),
    path('get_report_by_id/<int:id>/', ReportAPI.as_view(), name='get-report-by-id-api'),
    path('create_report/', ReportAPI.as_view(), name='create-report')
]
