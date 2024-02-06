from django.shortcuts import render
from django.http import HttpResponse

from portfolio.models import Project

# Create your views here.
def index(request):
    return render( request, 'core/index.html')
def about (request):
    return render(request,'core/about.html')
def portafolio(request):
    projects = Project.objects.all() 
    return render(request, "core/portafolio.html",{'projects':projects})

def contact (request):
    return render(request,'core/contact.html')