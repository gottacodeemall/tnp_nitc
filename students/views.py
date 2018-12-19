from django.shortcuts import render
from .models import FileUpload,StudentInstruction
# Create your views here.

def students(request):
    try:
        html=StudentInstruction.objects.all()
        html=html[0].instruction_html
        files=FileUpload.objects.all()
        count=files.count()
    except:
        return render(request, 'fail.html')
    return render(request, 'students.html',locals())