from django.urls import path
from pages import views #importing views from pages app

urlpatterns = [
    path('', views.about_me_view, name='about_me'),
    path('experience/', views.experience_view, name='experience'),

]