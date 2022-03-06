import django
from django.urls import URLPattern, path
from . import views

app_name = 'appPasswordGen'
urlpatterns = [
    path('home/', views.home, name="home"),
    path('password/', views.password, name="password"),
    path('about/', views.about, name="about")
]
