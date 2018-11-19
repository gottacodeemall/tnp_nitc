from django.urls import path
from . import views

urlpatterns = [
    path('aboutus', views.aboutus, name='about'),
    path('academics', views.academics, name='academics'),
    path('gallery', views.gallery, name='gallery'),
    path('achievements', views.achievements, name='achievements'),
]