from django import forms

from userManagement.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'description')


