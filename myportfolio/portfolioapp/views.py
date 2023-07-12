from django.shortcuts import render
from .models import MyProject

# Create your views here.
def portfolio(request) :
    proj = MyProject.objects.all()
    return render(request ,'index.html' , {'projects': proj})
