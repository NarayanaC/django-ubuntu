from django.shortcuts import HttpResponse, render

# Create your views here.
def ping(request):
    return HttpResponse('msg')