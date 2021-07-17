from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from boards import views

app_name = 'boards'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<board_name>[\w\-\ ]+)/$', views.topic, name='topic-list'),
]


