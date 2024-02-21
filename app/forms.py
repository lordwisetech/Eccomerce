
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput


# - Create/Register a user (Model Form)

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder': '   Enter your username '}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder': '      Enter your Email '}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder': '  Enter your password '}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder': '  confirm your password '}))



    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


# - Authenticate a user (Model Form)

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
