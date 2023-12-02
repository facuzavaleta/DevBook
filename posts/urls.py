from django.urls import path
from .views import delete_post

urlpatterns = [
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
]