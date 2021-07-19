from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")

    class Meta:
        model = User
        fields = ("username", "email", 'password1', 'password2' )
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=12)
    password = forms.CharField(widget=forms.PasswordInput())
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'