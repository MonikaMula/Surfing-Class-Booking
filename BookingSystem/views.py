from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'bookingsystem/home.html')

def classes(request):
    return render(request, 'bookingsystem/classes.html')

def customer(request):
    return render(request, 'bookingsystem/customer.html')