import django
from django.urls import URLPattern, path
from .import views

urlpatterns=[
    path('home/',views.tutors,name="home"),
    path('password/',views.tutors,name="password"),
    path('about/',views.tutors,name="about")

 ]