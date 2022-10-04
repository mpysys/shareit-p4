from django.shortcuts import render, HttpResponse

# Create your views here.


def homepage(request, *args, **kwargs):
    return HttpResponse("Hello World")
