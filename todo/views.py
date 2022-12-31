from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError



def home(request):
    return render(request, 'todo/home.html')


def SignUpUser(request):
    if request.method == "GET":
        return render(request, 'todo/SignUpUser.html', {'form':UserCreationForm()})
    else:
        # Create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('CurrentTodo')
            except IntegrityError:
                return render(request, 'todo/SignUpUser.html', {'form':UserCreationForm(), 'ERROR': 'The username has already been taken'})
        else:
            # Tell the user the password didn't match
            print('The password didn\'t match')
            return render(request, 'todo/SignUpUser.html', {'form':UserCreationForm(), 'ERROR': 'The password didn\'t math'})


def CurrentTodo(request):
    return render(request, 'todo/CurrentTodo.html')


def LogoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

    return render(request, 'todo/LogoutUser.html')
