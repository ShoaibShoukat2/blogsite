from django.urls import path
from .views import *


urlpatterns = [
    
    path('',index,name="index-page"),
    path('django/',MainDjango,name="MainDjango-page"),
    
    
    # Django Urls
    
    path('django/pythonanywhere/',PythonAnyWhere,name="PythonAnywhere-page"),
    path('django/staticconfiguration/',StaticTemplate,name="staticAndTemplateConfigure-page"),
    path('django/cpanel/',Cpanel,name="cpanel-page"),
    path('django/postgress-django/',PostgressDjango,name="postgressdjango-page"),
    
    
    
    # Node urls
    
    path('nodejs/',Node,name="node-page"),
    
    # Python urls
    
    path('python/',Python,name="python-page"),  
    path('python/beautiful-soup-vs-selenium/',BeauSele,name="beautifulsoupSelenium-page"),  
    
    
    # Javascript urls
    path('javascript/',Javascript,name="javascript-page"),

    
]









