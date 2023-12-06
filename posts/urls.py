from django.urls import path
from .views import delete_post, post_detail, delete_comment

urlpatterns = [
    path('<int:post_id>/delete/', delete_post, name='delete_post'),
    path('<int:post_id>/', post_detail, name='post_detail'),
    path('<int:post_id>/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]