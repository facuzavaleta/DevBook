from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login
from .forms import SignUpForm, UserLoginForm, EditProfileForm
from django.contrib.auth import logout
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from posts.models import Post
from django.contrib import messages

@login_required(login_url='login')
def home_view(request, username):
    user_profile = get_object_or_404(CustomUser, username=username)
    user_posts = Post.objects.filter(profile_owner=user_profile).order_by('-created_at')
    post_form = PostForm()

    # Agregamos el manejo de seguir/dejar de seguir
    is_following = request.user in user_profile.followers.all()
    followers = user_profile.followers.all()

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.posted_by = request.user
            new_post.profile_owner = user_profile
            new_post.save()
            return redirect('home', username=username)

    return render(request, 'users/home.html', {
        'username': username,
        'user_posts': user_posts,
        'post_form': post_form,
        'user_profile': user_profile,
        'is_following': is_following,
        'followers': followers,
    })

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

def user_search(request):
    query = request.GET.get('q')

    if query:
        results = CustomUser.objects.filter(username__icontains=query)
    else:
        results = None

    return render(request, 'users/user_search.html', {'query': query, 'results': results})

@login_required(login_url='login')
def user_detail(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, 'users/user_detail.html', {'user': user, 'username': username})

@login_required(login_url='login')
def edit_user(request, username):
    user = get_object_or_404(CustomUser, username=username)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', username=username)
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'users/edit_user.html', {'form': form, 'user': user, 'username': username})

def toggle_follow(request, username):
    user_to_follow = get_object_or_404(CustomUser, username=username)

    if request.user.is_authenticated:
        if request.user in user_to_follow.followers.all():
            # El usuario ya sigue a la persona, así que dejamos de seguir
            request.user.following.remove(user_to_follow)
        else:
            # El usuario no sigue a la persona, así que comenzamos a seguir
            request.user.following.add(user_to_follow)

    return redirect('home', username=username)
