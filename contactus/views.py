from django.shortcuts import render
from .models import ReachUs,ContactUs,People
# Create your views here.
def contactus(request):
    quickcontact=People.objects.filter(display_in_contactus=True)
    qc_count=quickcontact.count()
    info=ContactUs.objects.all()
    info=info[0]
    return render(request, 'contactus.html',locals())

def reachus(request):
    reachus=ReachUs.objects.all()
    reachus=reachus[0]
    return render(request, 'howtoreach.html',locals())

def people(request):
    faculty=People.objects.filter(role='Faculty')
    fac_count=faculty.count()
    core = People.objects.filter(role='Core Committee')
    core_count = core.count()
    rep = People.objects.filter(role='Placement Representative')
    rep_count = rep.count()
    return render(request, 'people.html',locals())