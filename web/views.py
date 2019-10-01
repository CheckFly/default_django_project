from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    message = "Welcome in my Page !"
    return HttpResponse(message)
