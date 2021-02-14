from django.shortcuts import render
from .models import Course

# Create your views here.


def home(request,name):
    course=Course.objects.get(Name=name)
    return render(request,"Home.html",{"course":course})

def getl(request,url):
  ur=Course.objects.get(Name=url)
  return render(request,"getlink.html",{"url":ur})
    
    