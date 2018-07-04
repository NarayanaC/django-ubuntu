from django.shortcuts import HttpResponse, render

# Create your views here.


def home(request):
    return HttpResponse('hello')

def hell(request):
    return HttpResponse('hello')

def bell(request):
    return HttpResponse('hello')
