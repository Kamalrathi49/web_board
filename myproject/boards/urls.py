from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from boards import views

app_name = 'boards'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new-board/$', views.add_board, name='new-board'),
    url(r'^delete-post/(?P<id>\d+)$', views.delete_post, name='delete-post'),
    url(r'^(?P<board_name>[\w\-\@\#\_ ]+)add/$', views.submit_form, name='add-topic'),   
    url(r'^(?P<board_name>[\w\-\@\#\_ ]+)/$', views.topic, name='topic-list'),
    url(r'^(?P<board_name>[\w\-\@\#\_ ]+)/(?P<topic_subject>[\w\-\ ]+)/(?P<topic_pk>\d+)/post/$', views.post, name='topic-post'),
    url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_post, name='reply-topic'),
]


