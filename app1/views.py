from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def function1(request):
    return HttpResponse('<marquee><h1>puli1</marquee></h1>')
