from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import NewPost
"""
generic views used to display data from database mpdels

"""
from django.views.generic import (ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
"""
Create a post or a blog
"""


class PostCreateView(LoginRequiredMixin, CreateView):
    model = NewPost
    fields = ['title', 'content']
    success_url = '/blog'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


"""
display all blogs in a listview container
"""


class PostListView(ListView):
    model = NewPost
    template_name = 'blog/NewPost_ListView.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #ordering = ['-date_posted']
    #paginate_by = 5


"""
display posts by a specific user only 
"""


class PostListView_by_author(ListView):
    model = NewPost
    template_name = 'blog/NewPost_ListView.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return NewPost.objects.filter(author=user).order_by('-date')


"""
click on a post and see detail ,
inherits from django generic view
called DetailView
"""


class PostDetailView(DetailView):
    model = NewPost


"""
update a post , but login is required ,
its inheriting from django generic view
called UpdateView
"""


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NewPost
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


"""
delete a post , inherits from django 
generic DeleteView
"""


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = NewPost
    success_url = ''

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'application': 'developer'})
