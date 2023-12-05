from django import forms
from .models import CustomUser, Project, ProjectComment

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link', 'repository_link', 'image']