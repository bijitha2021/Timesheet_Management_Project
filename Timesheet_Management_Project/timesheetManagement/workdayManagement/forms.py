import datetime
from django import forms
from django.core.exceptions import ValidationError

from workdayManagement.models import Workday


class WorkForm(forms.ModelForm):

    work_date = forms.DateField(initial=datetime.date.today)
    location = forms.CharField(max_length=30, required=True)
    user = forms.CharField(max_length=30, required=True)
    time_in = forms.TimeField()
    time_out = forms.TimeField()
    hours_code = forms.CharField(max_length=5)

    class Meta:
        model = Workday
        fields = ('work_date', 'location', 'user', 'time_in', 'time_out', 'hours_code')

