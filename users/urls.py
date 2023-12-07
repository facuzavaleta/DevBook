from django.urls import path, include
from .views import login_view, signup_view, logout_view, home_view, user_search, edit_user, user_detail, toggle_follow

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('search/', user_search, name='user_search'),
    path('<str:username>/', home_view, name='home'),
    path('<str:username>/detail/', user_detail, name='user_detail'),
    path('<str:username>/edit/', edit_user, name='edit_user'),
    path('<str:username>/toggle_follow/', toggle_follow, name='toggle_follow'),
    path('<str:username>/posts/', include('posts.urls')),
    path('<str:username>/projects/', include('projects.urls')),
]