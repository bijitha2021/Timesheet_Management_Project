from django import forms
from django.contrib.auth.models import User



from userManagement.models import User


class UserForm(forms.ModelForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    password=forms.CharField(max_length=30, required=False, help_text='Optional')


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'description','email','password')


