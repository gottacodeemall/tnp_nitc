from django.db import models

# Create your models here.
class StudentInstruction(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name to be displayed on Django admin. Do not create multiple instances.")
    instruction_html=models.TextField(blank=False,null=False,help_text="Enter the html content of the student instructions.")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

class FileUpload(models.Model):
    document = models.FileField(upload_to='static/files/')
    file_name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name")
    def __str__(self) -> str:
        return '{0}'.format(self.file_name)