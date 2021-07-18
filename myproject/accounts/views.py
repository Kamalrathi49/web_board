from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth import login as auth_login

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
        ctx = {'form' : form}
        return render(request, 'accounts/signup.html', ctx)


def logout(request):
    logout(request)


