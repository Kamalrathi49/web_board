from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from boards import views

app_name = 'boards'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post-update/(?P<id>\d+)/$', views.update_post, name='update-post'),
    url(r'^(?P<board_name>[\w\-\ ]+)add/$', views.submit_form, name='add-topic'),   
    url(r'^(?P<board_name>[\w\-\ ]+)/$', views.topic, name='topic-list'),
    url(r'^(?P<board_name>[\w\-\ ]+)/(?P<topic_subject>[\w\-\ ]+)/post/(?P<topic_pk>\d+)/(?P<post_id>\d+)/$', views.post, name='topic-post'),
    url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_post, name='reply-topic'),
]


