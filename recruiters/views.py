from django.shortcuts import render

# Create your views here.
def pastplacements(request):
    return render(request, 'pastplacements.html')

def pastrecruiters(request):
    return render(request, 'pastrecruiters.html')

def whyus(request):
    return render(request, 'whyus.html')

def pandp(request):
    return render(request, 'pandp.html')