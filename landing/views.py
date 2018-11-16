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

def recruiters(request):
    return render(request, 'recruiters.html')

def people(request):
    return render(request, 'people.html')

def students(request):
    return render(request, 'students.html')

def pastplacements(request):
    return render(request, 'pastplacements.html')

def contactus(request):
    return render(request, 'contactus.html')