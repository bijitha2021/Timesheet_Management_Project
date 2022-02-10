from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views.generic import ListView, CreateView

from workdayManagement.models import Workday

from workdayManagement.forms import WorkForm


class WorkList(ListView):
    model = Workday
    context_object_name = 'Work'
    template_name = 'workdayManagement/work_list.html'

class WorkCreate(CreateView):
    form_class = WorkForm
    template_name = 'workdayManagement/work_new.html'
    success_url = reverse_lazy('workdayManagement:work_list')
