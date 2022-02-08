from django.shortcuts import render

# Create your views here.
from userManagement.models import User
from django.views.generic import ListView, DetailView, CreateView




class UserList(ListView):
    model=User
    context_object_name='Users'
    template_name='userManagement/user_list.html'


class UserDetail(DetailView):
    model = User
    context_object_name = 'Users'
    template_name = 'userManagement/user_detail.html'



