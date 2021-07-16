from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    boards = Board.objects.all()
    ctx = {'boards':boards}
    return render(request, 'home.html',ctx)

def topic(request):
    topics = Topic.objects.all()
    ctx = {'topics': topics}
    return render(request, 'topic.html', ctx)
    