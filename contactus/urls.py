from django.urls import path
from . import views

urlpatterns = [
    path('people', views.people, name='people'),
    path('contactus', views.contactus, name='contactus'),
    path('reach', views.reachus, name='reachus'),
]