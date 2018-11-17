from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='about'),
    path('academics', views.academics, name='academics'),
    path('gallery', views.gallery, name='gallery'),
    path('achievements', views.achievements, name='achievements'),
    path('recruiters', views.pastrecruiters, name='pastrecruiters'),
    path('people', views.people, name='people'),
    path('students', views.students, name='students'),
    path('pastplacements', views.pastplacements, name='pastplacements'),
    path('contactus', views.contactus, name='contactus'),
    path('whyus', views.whyus, name='whyus'),
    path('pandp', views.pandp, name='pandp'),
]