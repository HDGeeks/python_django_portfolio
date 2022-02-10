from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def signUpUser(request):
    if request.method=='GET':
        return render(request,'appToDo_woo/signUp.html',{'signUpForm':UserCreationForm()})
    else:
        if request.method=='POST':
            if request.POST['password1']==request.POST['password2']:
                try:
                    user=User.objects.create_user(request.POST['username'],request.POST['password1'])
                    user.save()
                    login(request,user)
                    return redirect('home')
                except IntegrityError:
                    return render(request,'appToDo_woo/signUp.html',{'signUpForm':UserCreationForm(),'error':'username already exists'})    
            else:
                # let the user now either the username or password is wrong
                return render(request,'appToDo_woo/signUp.html',{'signUpForm':UserCreationForm(),'error':'password didnt match'})
def home(request):
    return render(request,'appToDo_woo/home.html')

                    

                

