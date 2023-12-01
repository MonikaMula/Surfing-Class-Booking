from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('home')

def classes(request):
    return HttpResponse('classes')

def customer(request):
    return HttpResponse('customer')