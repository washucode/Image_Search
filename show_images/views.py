from django.shortcuts import render
from django.conf.urls import url
from django.http import HttpResponse, Http404
from .models import Category,location,Image
# Create your views here.
def home(request):
   
    images = Image.allphotos()
    return render(request, 'allphotos.html')

    
