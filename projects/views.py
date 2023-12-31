from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Project, ProjectComment
from users.models import CustomUser
from .forms import ProjectForm, ProjectCommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def projects_index(request, username):
    user = get_object_or_404(CustomUser, username=username)
    is_owner = request.user == user
    user_projects = Project.objects.filter(user__username=username).order_by('-created_at')

    return render(request, 'projects/projects_index.html', {'username': username, 'is_owner': is_owner, 'user_projects': user_projects})

@login_required(login_url='login')
def create_project(request, username):
    project_form = ProjectForm()

    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            new_project = project_form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            return redirect('projects_index', username=request.user.username)
        else:
            project_form = ProjectForm()

    return render(request, 'projects/create_project.html', {'project_form': project_form})

@login_required(login_url='login')
def project_detail(request, username, project_id):
    project = get_object_or_404(Project, id=project_id, user__username=username)
    projectcomments = ProjectComment.objects.filter(project=project).order_by('created_at')

    if request.method == 'POST':
        projectcomment_form = ProjectCommentForm(request.POST)
        if projectcomment_form.is_valid():
            new_projectcomment = projectcomment_form.save(commit=False)
            new_projectcomment.user = request.user
            new_projectcomment.project = project
            new_projectcomment.save()
            return redirect('project_detail', username=username, project_id=project_id)
    else:
        projectcomment_form = ProjectCommentForm()

    return render(request, 'projects/project_detail.html', {'project': project, 'projectcomments': projectcomments, 'username': username, 'projectcomment_form': projectcomment_form})

@login_required(login_url='login')
def edit_project(request, username, project_id):
    user = get_object_or_404(CustomUser, username=username)
    project = get_object_or_404(Project, id=project_id, user__username=username)

    if request.method == 'POST':
        project_form = ProjectForm(request.POST, instance=project)
        if project_form.is_valid():
            project_form.save()
            return redirect('project_detail', username=username, project_id=project_id)
    else:
        project_form = ProjectForm(instance=project)

    return render(request, 'projects/edit_project.html', {'user': user, 'project_form': project_form})

@login_required(login_url='login')
def delete_project(request, username, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.user == project.user:
        project.delete()
        messages.success(request, 'El post ha sido eliminado con éxito.')
    else:
        messages.error(request, 'No tienes permisos para eliminar este post.')

    return redirect('projects_index', username=username)

@login_required(login_url='login')
def delete_projectcomment(request, username, project_id, projectcomment_id):
    projectcomment = get_object_or_404(ProjectComment, id=projectcomment_id, project__id=project_id)

    if request.user == projectcomment.user:
        projectcomment.delete()
        messages.success(request, 'El comentario ha sido eliminado con éxito.')
    else:
        messages.error(request, 'No tienes permisos para eliminar este comentario.')

    return redirect('project_detail', username=username, project_id=project_id)