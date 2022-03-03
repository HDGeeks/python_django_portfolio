from time import timezone
from xmlrpc.client import NOT_WELLFORMED_ERROR
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import create_new_form, Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def start(request):
    return render(request, 'appToDo_woo/start.html')


def signUpUser(request):
    if request.method == 'GET':
        return render(request, 'appToDo_woo/signUp.html',
                      {'signUpForm': UserCreationForm()})
    else:
        if request.method == 'POST':
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(request.POST['username'],
                                                    request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('home')
                except IntegrityError:
                    return render(
                        request, 'appToDo_woo/signUp.html', {
                            'signUpForm': UserCreationForm(),
                            'error': 'username already exists'
                        })
            else:
                # let the user now either the username or password is wrong
                return render(
                    request, 'appToDo_woo/signUp.html', {
                        'signUpForm': UserCreationForm(),
                        'error': 'password didnt match'
                    })


def loginUser(request):
    if request.method == 'GET':
        return render(request, 'appToDo_woo/userlogin.html',
                      {'loginForm': AuthenticationForm()})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'appToDo_woo/userlogin.html', {
                'loginForm': AuthenticationForm(),
                'error': 'password didnt match'
            })
        else:
            login(request, user)
            return redirect('home')


def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def home(request):
    todo_lists = Todo.objects.filter(user=request.user,
                                     datecompleted__isnull=True)
    return render(request, 'appToDo_woo/home.html', {'todoLists': todo_lists})


@login_required
def new_todo(request):
    if request.method == 'GET':
        return render(request, 'appToDo_woo/create_new.html',
                      {'create_new_form': create_new_form()})
    else:
        try:
            new_todo_form = create_new_form(request.POST)
            new_to_do = new_todo_form.save(commit=False)
            new_to_do.user = request.user
            new_to_do.save()
            return redirect('home')

        except ValueError:
            return render(
                request, 'appToDo_woo/create_new.html', {
                    'create_new_form':
                    create_new_form(),
                    'error':
                    'bad data type or exceeded the length specified of a specific field .'
                })


@login_required
def todo_detail(request, pk_Todo):
    to_detail = get_object_or_404(Todo, pk=pk_Todo, user=request.user)
    if request.method == 'GET':
        detailForm = create_new_form(instance=to_detail)
        return render(request, 'appToDo_woo/detail.html', {
            'deta': to_detail,
            'details_form': detailForm
        })
    else:
        try:
            detailForm = create_new_form(request.POST, instance=to_detail)
            detailForm.save()
            return redirect('home')
        except ValueError:
            return render(
                request, 'appToDo_woo/detail.html', {
                    'deta':
                    to_detail,
                    'details_form':
                    detailForm,
                    'error':
                    'bad data type or exceeded the length specified of a specific field .'
                })


@login_required
def delete_todo(request, pk_Todo):
    to_delete = get_object_or_404(Todo, pk=pk_Todo, user=request.user)
    if request.method == 'POST':
        to_delete.delete()
        return redirect('home')
    else:
        detailForm = create_new_form(instance=to_delete)
        return render(request, 'appToDo_woo/detail.html', {
            'deta': to_delete,
            'details_form': detailForm
        })


@login_required
def completed_task(request):
    tsks_done = Todo.objects.filter(
        user=request.user,
        datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'todo/completedtodos.html', {'todos': tsks_done})


@login_required
def completed(request, pk_Todo):
    to_complete = get_object_or_404(Todo, pk=pk_Todo, user=request.user)
    if request.method == 'POST':
        to_complete.datecompleted = timezone.now()
        to_complete.save()
        return redirect('home')
    else:
        detailForm = create_new_form(instance=to_complete)
        return render(request, 'appToDo_woo/detail.html', {
            'deta': to_complete,
            'details_form': detailForm
        })
