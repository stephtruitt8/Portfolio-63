from django.shortcuts import render
from .models import Project

# Create your views here.

def projects_view(request):
    projects_list = Project.objects.all().order_by('-year')  # Fetch all projects and order them by year in descending order
    context = {'projects': projects_list}
    return render(request, 'projects/projects.html', context)

