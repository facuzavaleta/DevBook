from django.urls import path, include
from .views import login_view, signup_view, logout_view, home_view, user_search

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('search/', user_search, name='user_search'),
    path('<str:username>/', home_view, name='home'),
    path('<str:username>/posts/', include('posts.urls')),
]