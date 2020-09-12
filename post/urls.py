from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.PostList.as_view(), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path(r'by/(?P<username>[-\W]+', views.UserPosts.as_view(), name='for_user'),
    path(r'by/(?P<username>[-\W]+(?P<pk>\d+)', views.PostDetail.as_view(), name='single'),
    path(r'delete//(?<pk>\d+)/', views.DeletePost.as_view(), name='delete'),
]