from django.shortcuts import render
from .models import FileUpload,StudentInstruction
# Create your views here.

def students(request):
    html=StudentInstruction.objects.all()
    html=html[0].instruction_html
    files=FileUpload.objects.all()
    count=files.count()
    return render(request, 'students.html',locals())