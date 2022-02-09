import django


from django.urls import URLPattern, path
from .import views
urlpatterns=[
    path('',views.tutors,name="TUTORIALS")

 ]