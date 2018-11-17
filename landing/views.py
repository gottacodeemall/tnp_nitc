from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def academics(request):
    return render(request, 'academics.html')

def gallery(request):
    return render(request, 'gallery.html')

def achievements(request):
    return render(request, 'achievements.html')

def people(request):
    return render(request, 'people.html')

def students(request):
    return render(request, 'students.html')

def pastplacements(request):
    return render(request, 'pastplacements.html')

def pastrecruiters(request):
    return render(request, 'pastrecruiters.html')

def whyus(request):
    return render(request, 'whyus.html')

def pandp(request):
    return render(request, 'pandp.html')

def contactus(request):
    return render(request, 'contactus.html')