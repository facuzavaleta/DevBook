from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login
from .forms import SignUpForm, UserLoginForm
from django.contrib.auth import logout
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from posts.models import Post
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home', username=user.username)
    else:
        form = SignUpForm()
    
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home', username=request.user.username)
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing')

@login_required
def home_view(request, username):
    user_profile = get_object_or_404(CustomUser, username=username)

    user_posts = Post.objects.filter(profile_owner=user_profile).order_by('-created_at')
    post_form = PostForm()

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.posted_by = request.user
            new_post.profile_owner = user_profile
            new_post.save()
            return redirect('home', username=username)

    return render(request, 'users/home.html', {'username': username, 'user_posts': user_posts, 'post_form': post_form})

def user_search(request):
    query = request.GET.get('q')

    if query:
        results = CustomUser.objects.filter(username__icontains=query)
    else:
        results = None

    return render(request, 'users/user_search.html', {'query': query, 'results': results})