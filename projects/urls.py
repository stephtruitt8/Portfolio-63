from django.urls import path
from projects import views #importing views from projects app

urlpatterns = [
    path('projects/', views.projects_view, name='projects'),
]