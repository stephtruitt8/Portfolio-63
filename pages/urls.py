from django.urls import path
from pages import views #importing views from pages app

urlpatterns = [
    path('', views.about_me_view, name='about_me'),
    path('experience/', views.experience_view, name='experience'),
    path('contact/', views.contact_view, name='contact'),
    path('blog/', views.blog_view, name='blog'),
    path('projects/', views.projects_view, name='projects')

]