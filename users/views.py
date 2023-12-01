from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login
from .forms import SignUpForm, UserLoginForm
from django.contrib.auth import logout
from .models import CustomUser

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirige al perfil del usuario recién registrado
            return redirect('home', username=user.username)
    else:
        form = SignUpForm()
    
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Redirige al perfil del usuario autenticado
            return redirect('home', username=request.user.username)
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing')

def home_view(request, username):
    user_profile = get_object_or_404(CustomUser, username=username)
    authenticated_username = request.user.username if request.user.is_authenticated else None
    return render(request, 'users/home.html', {'username': username, 'authenticated_username': authenticated_username})