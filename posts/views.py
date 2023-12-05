from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm
from users.models import CustomUser

@login_required
def post_detail(request, username, post_id):
    user_profile = get_object_or_404(CustomUser, username=username)
    post = get_object_or_404(Post, id=post_id, profile_owner=user_profile)
    comments = Comment.objects.filter(post=post).order_by('created_at')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return redirect('post_detail', username=username, post_id=post_id)
    else:
        comment_form = CommentForm()

    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

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
def delete_comment(request, username, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post__id=post_id)

    if request.user == comment.user or request.user == comment.post.profile_owner:
        comment.delete()
        messages.success(request, 'El comentario ha sido eliminado con éxito.')
    else:
        messages.error(request, 'No tienes permisos para eliminar este comentario.')

    return redirect('post_detail', username=comment.post.profile_owner.username, post_id=post_id)