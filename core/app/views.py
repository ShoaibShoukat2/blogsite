from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')




def MainDjango(request):

    return render(request,'Django/MainDjango.html')



def PythonAnyWhere(request):

    return render(request,'Django/pages/HostAnyWhere.html')


def StaticTemplate(request):
    
    
    return render(request,'Django/pages/StaticTemplate.html')


def Cpanel(request):
    
    return render(request,'Django/pages/Cpanel.html')


def PostgressDjango(request):
    
    return render(request,'Django/pages/PostgressDjango.html')


# Nodejs Functions


def Node(request):
    
    return render(request,'Not_Found.html')



# Python Functionss


def Python(request):
    
    return render(request,'Python/MainPython.html')




def BeauSele(request):
    
    
    return render(request,'Python/pages/Beautiful&Selenium.html')




















# Javascripte page

def Javascript(request):
    
    return render(request,'Not_Found.html')











