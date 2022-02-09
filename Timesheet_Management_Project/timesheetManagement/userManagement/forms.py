from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from userManagement.models import Doctor


class UserForm(forms.Form):
    firstname = forms.CharField(max_length=30, required=False)
    lastname = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(max_length=30, required=False)
    description = forms.CharField(max_length=30, required=False)
    image = forms.ImageField(required=False)


class Meta:
    model = Doctor
    fields = ('firstname', 'lastname', 'email', 'password1', 'password2', 'description', 'image')


class AuthUserCreateForm(UserCreationForm):
    firstname = forms.CharField(max_length=30, required=False)
    lastname = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(max_length=30, required=False)
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'password', 'username')


class DoctorCreateForm(forms.ModelForm):
    description = forms.CharField(max_length=30, required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = Doctor
        exclude = ('user',)
