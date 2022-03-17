from django import forms
from report.models import Report

class ReportForm(forms.ModelForm):
    class meta:
        model = Report
        fields = "__all__"