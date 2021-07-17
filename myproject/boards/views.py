from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    board_list = Board.objects.all()
    ctx = {'boards':board_list}
    return render(request, 'home.html',ctx)

def topic(request, board_name):
    topic_list = Topic.objects.filter(board__name = board_name)
    # board = Board.objects.get(name = board_name)
    ctx = {'topics': topic_list}
    return render(request, 'topic.html', ctx)
    