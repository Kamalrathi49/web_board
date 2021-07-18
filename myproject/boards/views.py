from django.core.checks import messages
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.shortcuts import redirect
from django.contrib import messages

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

def add_topic(request, board_name):
    return render( request, 'add_topic.html')

def submit_form1(request, board_name):
    if request.method == 'POST':
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        # b = request.META.get('HTTP_REFERER').split('/')[3]
        board = Board.objects.get(name=board_name)
        topic = Topic.objects.create(subject=sub, topic_message=msg, starter=request.user, board=board)
        topic.save()
        messages.success(request, f'{sub} topic  created successfully!') 
        return redirect(f'/{board_name}')
    else : 
        messages.error(request, f'something went') 
        return redirect(f'/{board_name}/add')

def submit_form(request, board_name):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid :
            topic = form.save(commit=False)
            topic.board = Board.objects.get(name=board_name)
            topic.starter = request.user
            topic.save()
            messages.success(request, f'{topic.subject} topic  created successfully!') 
            return redirect(f'/{board_name}')
        else :
            messages.error(request, f'something went wrong') 
            return redirect(f'/{board_name}/add')
    else : 
        form = TopicForm()
        ctx = {'form':form}
        return render( request, 'add_topic1.html', ctx)
