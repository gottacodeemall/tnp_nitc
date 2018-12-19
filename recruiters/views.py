from django.shortcuts import render
from .models import WhyUs,VisitedCompanies,Policy,ProcedureStep,PolicyFileUpload,PlacementFileUpload,ChartData,StatsTable
# Create your views here.
def pastplacements(request):
    try:
        files = PlacementFileUpload.objects.all()
        chartdata=ChartData.objects.all()
        statsdata=StatsTable.objects.all()
        count=files.count()
    except:
        return render(request, 'fail.html')
    return render(request, 'pastplacements.html',locals())

def pastrecruiters(request):
    try:
        comp=VisitedCompanies.objects.all().order_by('name')
    except:
        return render(request, 'fail.html')
    return render(request, 'pastrecruiters.html',locals())

def whyus(request):
    try:
        whyus=WhyUs.objects.all()
        whyus=whyus[0]
    except:
        return render(request, 'fail.html')
    return render(request, 'whyus.html',locals())

def pandp(request):
    try:
        policy=Policy.objects.all()
        policy=policy[0]
        proceduresteps=ProcedureStep.objects.all()
        files=PolicyFileUpload.objects.all()
    except:
        return render(request, 'fail.html')
    return render(request, 'pandp.html',locals())