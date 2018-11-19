from django.contrib import admin
from .models import StudentInstruction,FileUpload
# Register your models here.
admin.site.register(StudentInstruction)
admin.site.register(FileUpload)