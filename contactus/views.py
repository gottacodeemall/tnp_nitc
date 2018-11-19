from django.shortcuts import render

# Create your views here.
def contactus(request):
    return render(request, 'contactus.html')

def reachus(request):
    return render(request, 'howtoreach.html')

def people(request):
    return render(request, 'people.html')