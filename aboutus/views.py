from django.shortcuts import render
from .models import Academic,Gallery,Achievement,AboutUs,New
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
import requests
import json
def achievements(request):
    try:
        ach=Achievement.objects.all().order_by('-date')
    except:
        return render(request, 'fail.html')
    return render(request, 'achievements.html',locals())

def news(request):
    try:
        news = New.objects.all().order_by('-date')
        payload = []
        for item in news:
            payload.append(item.name)
        newscount = news.count()
        # ##try to contact server
        #payload = ['highest_package','intra-nit','adobe','oracle']
        url = 'http://tnp-cse.herokuapp.com/api/json/'
        response = requests.post(url, data=json.dumps(payload))
        print(response)
        lis = response.content
        lis = json.loads(lis)
        news_sorted = []
        for item in lis:
            try:
                cur_news =New.objects.get(name=item)
                news_sorted.append(cur_news)
            except:
                print("missed an instance")
        news=news_sorted
    except:
        return render(request, 'fail.html')
    return render(request, 'news.html',locals())

def newsitem(request,id):
    try:
        news = New.objects.get(name=id)
    except:
        return render(request, 'fail.html')
    return render(request, 'newsitem.html',locals())

