from django.shortcuts import render
from django.conf.urls import url
from django.http import HttpResponse, Http404
from .models import Category,location,Image
# Create your views here.
def home(request):
   
    images = Image.allphotos()
    return render(request, 'allphotos.html',{'images':images})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")

        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        
        

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

# def nairobi(request):
#     locationterm = 'nairobi'
#     location_images = Image.find_by_location(locationterm)
#     return render(request,'nairobi.html',{'images':location_images})


