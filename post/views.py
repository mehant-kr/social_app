# POST/views.py

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin
from .forms import PostForm

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model() 
# when someone is logged in the session then, 
# we're going to use User object of current user to call on the object


class PostList(SelectRelatedMixin, generic.ListView):
    template_name = "post/post_list.html"
    models = models.Post
    select_related = ('user', 'group')
    # select_related is a mixen, that allowes us to provide a tuple of related models
    # basicaly foregin key for this post for 'user' that it belongs to and 'group'
    # that it belongs to

    # def get_queryset(self):
    #     self.post_user = User.objects.all()
    #     return self.post_user.posts.all()

    def get_queryset(self):
        """Return the last five published questions."""
        return User.objects.all()


class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'post/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
            # ORM - Object Relationship Model
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post_user'] = self.post_user
    #     return context


class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.Post
    form_class = PostForm    # ← use your custom form here
    # remove or comment out: fields = ('message','group')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('post:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self ,*args, **kwargs):
        messages.success(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)