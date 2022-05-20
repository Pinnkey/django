from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world")

def templatehome(request):
    return render(request,'index.html',{'lname':"Nag"})


def add(request):
    a = int(request.POST["num1"])
    b = int(request.POST["num2"])
    c = a + b
    return render(request,'result.html',{'addition':c})
# Create your views here.
