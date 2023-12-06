from django.urls import path
from .views import projects_index, project_detail, create_project, edit_project, delete_project, delete_projectcomment

urlpatterns = [
    path('', projects_index, name='projects_index'),
    path('create/', create_project, name='create_project'),
    path('<int:project_id>/', project_detail, name='project_detail'),
    path('<int:project_id>/edit', edit_project, name='edit_project'),
    path('<int:project_id>/delete', delete_project, name='delete_project'),
    path('<int:project_id>/<int:projectcomment_id>/delete', delete_projectcomment, name='delete_projectcomment'),

]