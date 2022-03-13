from django.urls import URLPattern, path
from . import views
from .views import (PostDeleteView, PostListView, PostDetailView,
                    PostCreateView, PostUpdateView, PostListView_by_author)

app_name = 'blog'
urlpatterns = [
    path('home/new/', PostCreateView.as_view(), name="newpost_form"),
    path('', PostListView.as_view(), name="blog_home"),
    path('user/<str:username>',
         PostListView_by_author.as_view(),
         name="newpost_user_detail"),
    path('home/<int:pk>/', PostDetailView.as_view(), name="newpost_detail"),
    path('home/<int:pk>/update/',
         PostUpdateView.as_view(),
         name="newpost_update"),
    path('home/<int:pk>/delete/',
         PostDeleteView.as_view(),
         name="post_confirm_delete"),
    path('about/', views.about, name="blog_about"),
]
