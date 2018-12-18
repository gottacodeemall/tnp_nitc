from django.shortcuts import render
from .models import CurLink,Gallery,Achievement
# Create your views here.
def aboutus(request):
    return render(request, 'aboutus.html',locals())

def academics(request):
    links=CurLink.objects.all()
    for item in links:
        if(item.branch=="b-CSE"):
            bcse=item.url
        elif(item.branch=="m-CSE"):
            mcse=item.url
        elif (item.branch == "b-ECE"):
            bece = item.url
        elif (item.branch == "m-ECE"):
            mece = item.url
        elif (item.branch == "b-EEE"):
            beee = item.url
        elif (item.branch == "m-EEE"):
            meee = item.url
        elif (item.branch == "b-CE"):
            bce = item.url
        elif (item.branch == "m-CE"):
            mce = item.url
        elif (item.branch == "b-CH"):
            bch = item.url
        elif (item.branch == "m-CH"):
            mch = item.url
        elif (item.branch == "b-ME"):
            bme = item.url
        elif (item.branch == "m-ME"):
            mme = item.url
    return render(request, 'academics.html',locals())

def gallery(request):
    gal=Gallery.objects.all().order_by('-date')
    return render(request, 'gallery.html',locals())

def achievements(request):
    ach=Achievement.objects.all().order_by('-date')
    return render(request, 'achievements.html',locals())
 