from datetime import date
from django import forms

from workdayManagement.models import Workday


class WorkForm(forms.Form):

    work_date = forms.DateField()
    location = forms.CharField(max_length=30, required=False)
    user = forms.CharField(max_length=30, required=False)
    time_in = forms.TimeField()
    time_out = forms.TimeField()
    hours_code = forms.CharField(max_length=5)

    class Meta:
        model = Workday
        fields = ('work_date', 'location', 'user', 'time_in', 'time_out', 'hours_code')

