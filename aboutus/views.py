from django.shortcuts import render
from .models import Academic,Gallery,Achievement,AboutUs
# Create your views here.
def aboutus(request):
    try:
        aboutus=AboutUs.objects.all()
        aboutus=aboutus[0]
    except:
        return render(request, 'fail.html')
    return render(request, 'aboutus.html',locals())

def academics(request):
    try:
        btech=Academic.objects.filter(stream="B.Tech")
        mtech=Academic.objects.filter(stream="M.Tech")
        mca=Academic.objects.filter(stream="MCA")
        bc=btech.count()
        mc=mtech.count()
        mcc=mca.count()
        if (mc == 0 and bc == 0 and mcc == 0):
            return render(request, 'fail.html')
    except:
        return render(request, 'fail.html')
    return render(request, 'academics.html',locals())

def gallery(request):
    try:
        gal=Gallery.objects.all().order_by('-date')
    except:
        return render(request, 'fail.html')
    return render(request, 'gallery.html',locals())

def achievements(request):
    try:
        ach=Achievement.objects.all().order_by('-date')
    except:
        return render(request, 'fail.html')
    return render(request, 'achievements.html',locals())