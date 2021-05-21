# This file is created by me
from django.shortcuts import render
from django.http import HttpResponse    
def index(request):
    return render(request,'index.html')
