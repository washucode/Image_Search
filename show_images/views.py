from django.shortcuts import render
from django.conf.urls import url
from django.http import HttpResponse, Http404

# Create your views here.
def home(request):
    return HttpResponse('Welcome to Pictures')