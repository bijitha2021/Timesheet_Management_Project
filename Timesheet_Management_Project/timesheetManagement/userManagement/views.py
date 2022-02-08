from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.urls import reverse
from userManagement.models import User
from django.views.generic import ListView, DetailView, CreateView
from userManagement.forms import UserForm

# Create your views here.

class UserList(ListView):
    model=User
    context_object_name='Users'
    template_name='userManagement/user_list.html'


class UserDetail(DetailView):
    model = User
    context_object_name = 'Users'
    template_name = 'userManagement/user_detail.html'


def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user.save()
            return HttpResponseRedirect(reverse('userManagement:user_list'))
        else:
            return render(request, 'userManagement/user_new.html', {'form1': form})
    else:
        form = UserForm()
        return render(request, 'userManagement/user_new.html', {'form1': form})

