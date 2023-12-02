from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # Verificar si el usuario logueado es el propietario del post o tiene permisos para eliminar
    if request.user == post.posted_by or request.user == post.profile_owner:
        post.delete()
        messages.success(request, 'El post ha sido eliminado con éxito.')
    else:
        messages.error(request, 'No tienes permisos para eliminar este post.')

    return redirect('home', username=post.profile_owner.username)