from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm
from users.models import CustomUser

@login_required
def delete_post(request, username, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.user == post.posted_by or request.user == post.profile_owner:
        post.delete()
        messages.success(request, 'El post ha sido eliminado con éxito.')
    else:
        messages.error(request, 'No tienes permisos para eliminar este post.')

    return redirect('home', username=post.profile_owner.username)

@login_required
def post_detail(request, username, post_id):
    user_profile = get_object_or_404(CustomUser, username=username)
    post = get_object_or_404(Post, id=post_id, profile_owner=user_profile)
    comments = Comment.objects.filter(post=post)

    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})