from os import name
from django.urls import path
from django.conf.urls import url
from accounts import views
from django.contrib.auth import login, views as auth_views

app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.signup, name='sign-up'),
    # url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='log-in'),
    # url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^login/$', views.log_in, name='log-in')

]
