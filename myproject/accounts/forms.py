from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields
from django.forms.widgets import EmailInput, TextInput

class RegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
     'class': 'form-control', 'placeholder': 'Username'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
     'class': 'form-control', 'placeholder': 'Email Address'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',  'placeholder': 'Password'}),label=(u'Password'))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm Password'}),label=(u'Confirm Password'))
    class Meta:
        model = User
        fields = ("username", "email", 'password1', 'password2' )
    
    def __init__(self, *args, **kwargs):
        # Call to ModelForm constructor
        super(RegisterForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class LoginForm(forms.Form):
    username = forms.CharField(max_length=99, widget=forms.TextInput(attrs={
        'class': 'form-control',  'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',  'placeholder': 'Password'}))
    
    