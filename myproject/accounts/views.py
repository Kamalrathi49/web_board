from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, f'thankyou for signup {request.user}')
            return redirect('/')
        else :
            messages.error(request, f'something went wrong')
            return redirect(request.META.HTTP_REFERER)
    else:
        form = RegisterForm()
        ctx = {'form' : form}
        return render(request, 'accounts/signup.html', ctx)


def log_out(request):
    logout(request)
    messages.success(request,'you are succefully logout')
    return redirect('/')

from django.contrib.auth import authenticate, login
1

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request,f'welcome back {username}')
                return redirect('/')
            else:
                messages.error(request,f'user not exist')
                return redirect('log-in')


        else :
            messages.error(request, f'something went wrong')
            return redirect('/')
    else:
        form = LoginForm()
        ctx = {'form' : form}
        return render(request, 'accounts/login.html', ctx)
    
