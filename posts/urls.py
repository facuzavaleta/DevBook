from django.urls import path
from .views import delete_post, post_detail

urlpatterns = [
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('<int:post_id>/', post_detail, name='post_detail'),
]