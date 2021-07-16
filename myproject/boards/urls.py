from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('boards/topic/', views.topic, name='topic'),
]
