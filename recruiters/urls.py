from django.urls import path
from . import views

urlpatterns = [
    path('recruiters', views.pastrecruiters, name='pastrecruiters'),
    path('pastplacements', views.pastplacements, name='pastplacements'),
    path('whyus', views.whyus, name='whyus'),
    path('pandp', views.pandp, name='pandp'),
]