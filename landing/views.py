from django.shortcuts import render
from .models import Slide,WelcomeMessage,FromtheTPO,LandingStat
from aboutus.models import New
# Create your views here.

def index(request):
    try:
        slides=Slide.objects.all().order_by('number')
        slidescount=slides.count()
        welcomemsg=WelcomeMessage.objects.all()
        welcomemsg=welcomemsg[0]
        fromthetpo=FromtheTPO.objects.all()
        fromthetpo=fromthetpo[0]
        landingstat=LandingStat.objects.all()
        news = New.objects.all().order_by('-date')
        news =news[:5]
        newscount = news.count()
    except:
        return render(request, 'fail.html')
    return render(request, 'index.html',locals())




