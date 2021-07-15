from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Create your views here.

def home(request):
    a = Board.objects.all()
    username = ''
    page_name = 'Board'
    ctx ={'board':a, 'username': username, 'page': page_name}
    return render(request, 'home.html',ctx)