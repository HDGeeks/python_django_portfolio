from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .add_email_file import UserRegisterForm


def register(request):
    if request.method == 'POST':
        new_user_form = UserRegisterForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            username = new_user_form.cleaned_data.get('username')
            messages.success(
                request,
                f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        new_user_form = UserRegisterForm()
    return render(request, 'users_app/register.html',
                  {'create_new_user_form': new_user_form})


@login_required
def profile(request):
    return render(request, 'users_app/profile.html')
