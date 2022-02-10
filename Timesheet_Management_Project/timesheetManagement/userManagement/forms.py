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
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
#     password = forms.CharField(max_length=30, required=False) # We don't need this since UserCreationForm has password1 and password2 already .. but does not have first name, last name and email.. so those fields makes sense .
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2','username','is_superuser','is_staff','is_active')


class DoctorCreateForm(forms.ModelForm):
    description = forms.CharField(max_length=30, required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = Doctor
        exclude = ('user',)
        
