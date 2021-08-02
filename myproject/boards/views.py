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
    ctx = {'boards':board_list, 'login_form':loginform, 'signup_form': signupform}
    return render(request, 'home.html',ctx)

def topic(request, board_name):
    topic_list = Topic.objects.filter(board__name = board_name).order_by('-created_at')
    # board = Board.objects.get(name = board_name)
    ctx = {'topics': topic_list, 'login_form':loginform, 'signup_form': signupform}
    return render(request, 'topic.html', ctx)

def add_topic(request, board_name):
    return render( request, 'add_topic.html')

# def submit_form1(request, board_name):
#     if request.method == 'POST':
#         sub = request.POST.get('subject')
#         msg = request.POST.get('message')
#         # b = request.META.get('HTTP_REFERER').split('/')[3]
#         board = Board.objects.get(name=board_name)
#         topic = Topic.objects.create(subject=sub, topic_message=msg, starter=request.user, board=board)
#         topic.save()
#         messages.success(request, f'{sub} topic  created successfully!') 
#         return redirect(f'/{board_name}')
#     else : 
#         messages.error(request, f'something went') 
#         return redirect(f'/{board_name}/add')

@login_required
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
            return redirect(f'/{board_name}')
        else :
            messages.error(request, f'something went wrong') 
            return redirect(f'/{board_name}/add')
    else : 
        form = TopicForm()
        ctx = {'form':form}
        return render( request, 'add_topic1.html', ctx)
        
def post(request, board_name,  topic_subject, topic_pk):
    topic = Topic.objects.get(pk=topic_pk)
    ctx = {'topic': topic, 'login_form':loginform, 'signup_form': signupform}
    return render(request, 'topic_post.html', ctx )


