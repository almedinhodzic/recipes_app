from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistationForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user =  authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in.')
            return redirect('recipes')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('login_user')


def register_user(request):
    if request.method == 'POST':
        form = UserRegistationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'User successfully created.')
            return redirect('recipes')
    else:
        form = UserRegistationForm()

    return render(request, 'registration/register.html', {'form': form})