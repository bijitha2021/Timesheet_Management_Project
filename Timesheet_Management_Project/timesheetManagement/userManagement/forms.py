from django import forms
from django.contrib.auth.models import User



from userManagement.models import User


class UserForm(forms.ModelForm):

    firstname = forms.CharField(max_length=30, required=False)
    lastname = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    password=forms.CharField(max_length=30, required=False)


    class Meta:
        model = User
        fields = ('firstname','lastname','email','password','description','image')


