from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta: #information about the class
        model = User
        fields = [ 'username', 'email' , 'password' ]
