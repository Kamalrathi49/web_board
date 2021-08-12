from django.core.checks import messages
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from accounts.forms import *
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

loginform = LoginForm()
signupform = RegisterForm()


def home(request):
    board_list = Board.objects.all()
    board_form = BoardForm()
    ctx = {'boards':board_list, 'board_form':board_form, 'login_form':loginform, 'signup_form': signupform}
    return render(request, 'home.html',ctx)

def topic(request, board_name):
    topic_list = Topic.objects.filter(board__name = board_name).order_by('-created_at')
    topic_form = TopicForm()
    ctx = {'topics': topic_list, 'login_form':loginform, 'signup_form': signupform, 'topic_form':topic_form}
    return render(request, 'topic.html', ctx)

def add_board(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save()
            messages.success(request, f'Your Board "{board.name}" is added Successfully!')
            return redirect('/')

        else:
            messages.error(request, f'Board name must be unique!') 
            return redirect('/')
    
    else:
        messages.error(request, f'something went wrong') 
        return redirect('/')


def submit_form(request, board_name):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid :
            topic = form.save(commit=False)
            topic.board = Board.objects.get(name=board_name)
            topic.starter = request.user
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            messages.success(request, f'Your topic "{topic.subject}" is added Successfully!') 
            return redirect(request.META.get('HTTP_REFERER'))
        else :
            messages.error(request, f'something went wrong') 
            return redirect(request.META.get('HTTP_REFERER'))
    else : 
        messages.error(request, f'something went wrong') 
        return redirect('/')
        
def post(request, board_name, topic_subject, topic_pk):
    topic = Topic.objects.get(pk=topic_pk)
    post = Post.objects.filter(topic__pk=topic_pk)
    post_form = PostForm()
    ctx = {'topic': topic,'post':post, 'post_form':post_form, 'login_form':loginform, 'signup_form': signupform}
    return render(request, 'topic_post.html', ctx )


def reply_post(request, pk, topic_pk):
    topic = Topic.objects.get( board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            messages.success(request, f'Message added successfully!') 
            return redirect(request.META.get('HTTP_REFERER'), pk=pk, topic_pk=topic_pk)
        else:
            messages.error(request, f'Something went wrong! please try again!') 
            return redirect(request.META.get('HTTP_REFERER'))




def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    messages.success(request, f"Your Reply {post.message} deleted successfully!")
    return redirect(request.META.get('HTTP_REFERER'))