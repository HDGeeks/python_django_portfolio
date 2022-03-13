from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .users_forms import UserRegisterForm
"""
Create new user using the register function ,
If and only method is POST ,
if not , just return the form .
BTW , we are using UserRegisterForm inherited from users_forms
bcz i wanted to add an email field to the field of 
UserCreationForm . wink wink .

"""


def register(request):
    if request.method == 'POST':
        new_user_form = UserRegisterForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            username = new_user_form.cleaned_data.get('username')
            messages.success(
                request,
                f'Your account has been created! You are now able to log in')
            return redirect('users_app:all_start')
    else:
        new_user_form = UserRegisterForm()
    return render(request, 'users_app/register.html',
                  {'create_new_user_form': new_user_form})


@login_required
def profile(request):
    return render(request, 'users_app/profile.html')


def start(request):
    return render(request, 'users_app/all_start.html')
