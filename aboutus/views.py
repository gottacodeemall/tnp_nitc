from django.shortcuts import render

# Create your views here.
def aboutus(request):
    return render(request, 'aboutus.html')

def academics(request):
    return render(request, 'academics.html')

def gallery(request):
    return render(request, 'gallery.html')

def achievements(request):
    return render(request, 'achievements.html')
