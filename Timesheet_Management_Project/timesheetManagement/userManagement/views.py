from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.urls import reverse, reverse_lazy
from userManagement.models import Doctor
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from userManagement.forms import UserForm

# Create your views here.
from userManagement.forms import AuthUserCreateForm, DoctorCreateForm


class UserList(ListView):
    model = Doctor
    context_object_name = 'Users'
    template_name = 'userManagement/user_list.html'


class UserDetail(DetailView):
    model = Doctor
    context_object_name = 'Users'
    template_name = 'userManagement/user_detail.html'


def user_new(request):
    if request.method == "POST":
        # form = UserForm(request.POST)
        authuser = AuthUserCreateForm(request.POST)
        doctform = DoctorCreateForm(request.POST)

        if authuser.is_valid() and doctform.is_valid():
            user = authuser.save()
            doctform.user = user
            doctform.save()
            return HttpResponseRedirect(reverse('userManagement:user_list'))
        else:
            return render(request, 'userManagement/user_new.html', {'form': doctform})
    else:
        form = UserForm()
        return render(request, 'userManagement/user_new.html', {'form': form})


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
