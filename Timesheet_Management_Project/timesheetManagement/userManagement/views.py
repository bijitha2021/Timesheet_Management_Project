from itertools import chain
from operator import attrgetter

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from django.urls import reverse, reverse_lazy
from userManagement.models import Doctor
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from userManagement.forms import UserForm

# Create your views here.
from userManagement.forms import AuthUserCreateForm, DoctorCreateForm


class UserList(ListView):

    context_object_name = 'Users'
    template_name = 'userManagement/user_list.html'

    def get_queryset(self):
        queryset = Doctor.objects.select_related('user')
        return queryset

    

class UserDetail(DetailView):
    model = Doctor
    context_object_name = 'Users'
    template_name = 'userManagement/user_detail.html'


def user_new(request):
    if request.method == "POST":
        # form = UserForm(request.POST)
        authuserform = AuthUserCreateForm(request.POST)
        doctorform = DoctorCreateForm(request.POST)
        print(authuserform, doctorform)

        if authuserform.is_valid() and doctorform.is_valid():

            user = authuserform.save()            
            doctor = doctorform.save(commit=False)
            doctor.user = user
            doctorform.save()
            return HttpResponseRedirect(reverse('userManagement:user_list'))
        else:
            print(authuserform.is_valid(),doctorform.is_valid())
            return render(request, 'userManagement/user_new.html', {'authuserform': authuserform, 'doctorform': doctorform})
    else:
        authuserform = AuthUserCreateForm()
        doctorform = DoctorCreateForm()
        return render(request, 'userManagement/user_new.html', {'authuserform': authuserform, 'doctorform': doctorform}) # template will receive these 2 forms 


class UserCreate(CreateView):
    form_class = UserForm
    template_name = 'userManagement/user_new.html'
    success_url = reverse_lazy('userManagement:user_list')


def user_update(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    form = UserForm(request.POST or None, instance=user)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            user.save()
            return HttpResponseRedirect(reverse('userManagement:user_list'))
    else:
        return render(request, 'userManagement/user_update.html', {'form': form})


class UserUpdate(UpdateView):
    form_class = UserForm
    template_name = 'userManagement/user_update.html'
    success_url = reverse_lazy('userManagement:user_list')

def home_view(request):
    return render(request, 'userManagement/welcomepage.html')
