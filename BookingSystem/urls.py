from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('classes/', views.classes),
    path('customer/', views.customer),
]
