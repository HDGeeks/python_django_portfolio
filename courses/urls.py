import django

from django.urls import URLPattern, path
from . import views

app_name = 'courses'
urlpatterns = [path('', views.tutors, name="tutors")]
