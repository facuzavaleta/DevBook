from django.urls import path
from .views import login_view, signup_view, logout_view, home_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('<str:username>/', home_view, name='home'),
]