from django.urls import path
from . import views

urlpatterns = [
    path('aboutus', views.aboutus, name='about'),
    path('academics', views.academics, name='academics'),
    path('gallery', views.gallery, name='gallery'),
    path('achievements', views.achievements, name='achievements'),
    path('news', views.news, name='news'),
    path('news/<str:id>',views.newsitem,name='newsitem'),
]