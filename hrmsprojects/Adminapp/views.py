from django.shortcuts import HttpResponse, render

# Create your views here.
def adminapp(request):
    return HttpResponse('admin page')