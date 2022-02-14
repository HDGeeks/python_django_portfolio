import django
from django.urls import URLPattern, path
from appToDo_woo import views
from .models import Todo

#create your patterns here

urlpatterns=[
    path('signUp/',views.signUpUser,name="signUp"),
    path('home/',views.home,name="home"),
    path('home/<int:pk_Todo>',views.todo_detail,name="detail"),
    path('home/<int:pk_Todo>/complete',views.completed,name="complete"),
    path('create/',views.new_todo,name="create_new"),
    path('logout/',views.logoutUser,name="logoutUser"),
    path('login/',views.loginUser,name="loginUser")
]
