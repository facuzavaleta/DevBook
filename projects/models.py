from django.db import models
from users.models import CustomUser
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    repository_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

class ProjectComment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content= models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
