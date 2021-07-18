from django.urls import path
from django.conf.urls import url
from accounts import views

app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.signup, name='sign-up')
]
