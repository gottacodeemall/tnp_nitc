from django.shortcuts import render
from .models import ReachUs,ContactUs,People
# Create your views here.
def contactus(request):
    try:
        quickcontact=People.objects.filter(display_in_contactus=True)
        qc_count=quickcontact.count()
        info=ContactUs.objects.all()
        info=info[0]
    except:
        return render(request, 'fail.html')
    return render(request, 'contactus.html',locals())

def reachus(request):
    try:
        reachus=ReachUs.objects.all()
        reachus=reachus[0]
    except:
        return render(request, 'fail.html')
    return render(request, 'howtoreach.html',locals())

def people(request):
    try:
        faculty=People.objects.filter(role='Faculty')
        fac_count=faculty.count()
        core = People.objects.filter(role='Core Committee')
        core_count = core.count()
        rep = People.objects.filter(role='Placement Representative')
        rep_count = rep.count()
    except:
        return render(request, 'fail.html')
    return render(request, 'people.html',locals())