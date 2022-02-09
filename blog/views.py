from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import NewPost


def home(request):
    context = {
        'posts': NewPost.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = NewPost
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #ordering = ['-date_posted']
    paginate_by = 5


class DetailPostListView(ListView):
    model = NewPost
    template_name = 'blog/newpost_user_detail.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5 

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return NewPost.objects.filter(author=user).order_by('-date')


class PostDetailView(DetailView):
    model = NewPost


class PostCreateView(LoginRequiredMixin, CreateView):
    model = NewPost
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = NewPost
    success_url = '/home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'application': 'developer'})
