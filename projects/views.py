from django.shortcuts import render, get_object_or_404
from .models import Project
from users.models import CustomUser

# Create your views here.
def projects_index(request, username):
    # Obtén el usuario asociado al nombre de usuario proporcionado
    user = get_object_or_404(CustomUser, username=username)

    # Obtén todos los proyectos asociados al usuario
    projects = Project.objects.filter(user=user)
    is_owner = request.user == user
    # Renderiza la plantilla con los proyectos
    return render(request, 'projects/projects_index.html', {'username': username,'user': user, 'projects': projects, 'is_owner': is_owner})