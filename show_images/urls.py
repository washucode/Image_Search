from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.home, name="allphotos"),
    url('^search/',views.search_results, name="search_results"),
    url('^location/',views.nairobi,name= "nairobi"),
    url('^location/',views.mombasa,name= "mombasa"),
    url('^location/',views.upcountry,name= "upcountry"),
    url('^location/',views.other,name= "other"),
    url('^location/',views.out,name= "out"),

    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)