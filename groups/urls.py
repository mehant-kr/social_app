# GROUPS URLS.py
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    url(r'^posts/in/(?P<slug>[-\w]+)/$', views.SingleGroup.as_view(), name='single'),
    url(r'^join/(?P<slug>[-\w]+)/$', views.JoinGroup.as_view(), name='join'),
    url(r'^leave/(?P<slug>[-\w]+)/$', views.LeaveGroup.as_view(), name='leave'),

]