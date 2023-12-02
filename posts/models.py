from django.db import models
from users.models import CustomUser
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    profile_owner = models.ForeignKey(CustomUser, related_name='profile_owner', on_delete=models.CASCADE)
    posted_by = models.ForeignKey(CustomUser, related_name='posted_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home', kwargs={'username': self.user.username})
    
    def __str__(self):
        return f'{self.title} - {self.user.username}'
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"