from django.shortcuts import render, get_object_or_404
from .models import Project
from users.models import CustomUser

# Create your views here.
def projects_index(request, username):
    user = get_object_or_404(CustomUser, username=username)
    is_owner = request.user == user
    return render(request, 'projects/projects_index.html', {'username': username, 'is_owner': is_owner})