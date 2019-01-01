from django.shortcuts import render
from .models import WhyUs,VisitedCompanies,Policy,ProcedureStep,PolicyFileUpload,StatisticsFileUpload,ChartData,StatsTable
# Create your views here.
def pastplacements(request):
    try:
        files = StatisticsFileUpload.objects.all()
        chartdata=ChartData.objects.all()
        statsdata=StatsTable.objects.all().order_by('number')
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
        proceduresteps=ProcedureStep.objects.all().order_by('number')
        files=PolicyFileUpload.objects.all()
        filecount=files.count()
    except:
        return render(request, 'fail.html')
    return render(request, 'pandp.html',locals())