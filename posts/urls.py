from django.urls import path
from .views import delete_post, post_detail, delete_comment

urlpatterns = [
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('<int:post_id>/', post_detail, name='post_detail'),
    path('delete_comment/<str:username>/<int:post_id>/<int:comment_id>/', delete_comment, name='delete_comment'),
]