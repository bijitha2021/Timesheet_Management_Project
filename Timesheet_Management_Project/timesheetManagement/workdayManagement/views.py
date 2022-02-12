from django.db.models import Model
from django.forms import ModelForm
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView

from workdayManagement.models import Workday

from workdayManagement.forms import WorkForm




class WorkList(ListView):
    model = Workday
    context_object_name = 'Work'
    template_name = 'workdayManagement/work_list.html'


class WorkCreate(CreateView):
    model = Workday
    #form_class = WorkForm
    fields = ('work_date', 'location', 'user', 'time_in', 'time_out', 'hours_code')
    template_name = 'workdayManagement/work_new.html'
    success_url = reverse_lazy('workdayManagement:work_list')



class WorkUpdate(UpdateView):
    model = Workday
    fields = ('work_date', 'location', 'user', 'time_in', 'time_out', 'hours_code')
    template_name = 'workdayManagement/work_update.html'
    success_url = reverse_lazy('workdayManagement:work_list')


def Work_Update(request, work_id):

    #work = get_object_or_404(Workday, pk=work_id)
    work = Workday.objects.get(pk=work_id)
    form = WorkForm(request.POST or None,instance=work)

    if request.method == "POST":
        if form.is_valid():
            work = form.save()
            work.save()
            return HttpResponseRedirect(reverse('workdayManagement:work_list'))
    else:
        return render(request, 'workdayManagement/work_update.html', {'form': form})

