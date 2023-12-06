from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, ProjectComment
from users.models import CustomUser
from .forms import ProjectForm

# Create your views here.
def projects_index(request, username):
    user = get_object_or_404(CustomUser, username=username)
    is_owner = request.user == user
    user_projects = Project.objects.filter(user__username=username)

    return render(request, 'projects/projects_index.html', {'username': username, 'is_owner': is_owner, 'user_projects': user_projects})

def create_project(request, username):
    project_form = ProjectForm()

    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            new_project = project_form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            return redirect('projects_index', username=request.user.username)

    return render(request, 'projects/create_project.html', {'project_form': project_form})

def project_detail(request, username, project_id):
    user = get_object_or_404(CustomUser, username=username)
    project = get_object_or_404(Project, id=project_id, user__username=username)
    comments = ProjectComment.objects.filter(project=project).order_by('created_at')

    return render(request, 'projects/project_detail.html', {'user': user, 'project': project, 'comments': comments, 'username': username})

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