from django.shortcuts import render
from .models import Slide,WelcomeMessage,FromtheTPO,LandingStat
# Create your views here.

def index(request):
    try:
        slides=Slide.objects.all().order_by('number')
        welcomemsg=WelcomeMessage.objects.all()
        welcomemsg=welcomemsg[0]
        fromthetpo=FromtheTPO.objects.all()
        fromthetpo=fromthetpo[0]
        landingstat=LandingStat.objects.all()
    except:
        return render(request, 'fail.html')
    return render(request, 'index.html',locals())






