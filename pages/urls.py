from django.urls import path
from .views import landing_view, about_view

urlpatterns = [
    path('', landing_view, name='landing'),
    path('about/', about_view, name='about'),
]