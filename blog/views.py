from django.shortcuts import render

from .models import BlogPost

def home(request):
    return render(request, 'home.html', {'posts': BlogPost.objects.all()})