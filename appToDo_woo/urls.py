import django
from django.urls import URLPattern, path
from appToDo_woo import views

#create your patterns here

urlpatterns=[
    path('signUp/',views.signUpUser,name="signUp"),
    path('home/',views.home,name="home"),
    path('logout/',views.logoutUser,name="logoutUser"),
    path('login/',views.loginUser,name="loginUser")
]
