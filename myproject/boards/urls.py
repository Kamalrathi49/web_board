from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from boards import views

app_name = 'boards'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^submit-form/(?P<board_name>[\w\-\ ]+)$', views.submit_form, name='submit-form'),
    url(r'^(?P<board_name>[\w\-\ ]+)/$', views.topic, name='topic-list'),
    url(r'^(?P<board_name>[\w\-\ ]+)/add/$', views.submit_form, name='add-topic'),
    url(r'^topic/(?P<topic_pk>\d+)/$', views.post, name='topic-post'),
]


