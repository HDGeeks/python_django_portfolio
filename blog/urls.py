from django.urls import URLPattern, path
from .import views
from .views import (
    PostDeleteView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    DetailPostListView)
  
urlpatterns=[
    path('home/',PostListView.as_view(),name="blog_home"),
    path('user/<str:username>',DetailPostListView.as_view(),name="newpost_user_detail"),
    path('home/<int:pk>/',PostDetailView.as_view(),name="newpost_detail"),
    path('home/<int:pk>/update/',PostUpdateView.as_view(),name="newpost_update"),
    path('home/<int:pk>/delete/',PostDeleteView.as_view(),name="post_confirm_delete"),
    path('home/new/',PostCreateView.as_view(),name="newpost_form"),
    path('about/',views.about,name="blog_about"),
    ]
