from django.shortcuts import render
from .models import WhyUs,VisitedCompanies,Policy,ProcedureStep,PolicyFileUpload,PlacementFileUpload,ChartData,StatsTable
# Create your views here.
def pastplacements(request):
    files = PlacementFileUpload.objects.all()
    chartdata=ChartData.objects.all()
    statsdata=StatsTable.objects.all()
    count=files.count()
    return render(request, 'pastplacements.html',locals())

def pastrecruiters(request):
    comp=VisitedCompanies.objects.all().order_by('name')
    return render(request, 'pastrecruiters.html',locals())

def whyus(request):
    whyus=WhyUs.objects.all()
    whyus=whyus[0]
    return render(request, 'whyus.html',locals())

def pandp(request):
    policy=Policy.objects.all()
    policy=policy[0]
    proceduresteps=ProcedureStep.objects.all()
    files=PolicyFileUpload.objects.all()
    return render(request, 'pandp.html',locals())