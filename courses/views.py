from django.shortcuts import render
from django.http import HttpResponse
from .models import Courses

#subjects={[]}

# Create your views here.

def tutors(request):

    jobs=Courses.objects.all
    return render(request,'courses/courses.html',{'job':jobs})
 