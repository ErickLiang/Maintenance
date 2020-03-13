from django.shortcuts import render, HttpResponse
from .models import Server, Project
# Create your views here.

def index(request):
    all_project = Project.objects.all()

    return render(request, 'index.html', locals())