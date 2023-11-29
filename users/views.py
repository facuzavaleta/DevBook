from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, UserLoginForm
from django.contrib.auth import logout

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Reemplaza 'home' con tu vista de inicio
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
