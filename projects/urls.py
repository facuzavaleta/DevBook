from django.urls import path
from .views import projects_index, project_detail

urlpatterns = [
    path('', projects_index, name='projects_index'),
    path('<int:project_id>/', project_detail, name='project_detail')
]