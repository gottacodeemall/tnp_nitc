from django.db import models

# Create your models here.
class StudentInstruction(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name to be displayed on Django admin. Do not create multiple instances.")
    aboutus=models.TextField(blank=False,null=False,help_text="Enter the html content of the student instrcutions.")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

class FileUpload(models.Model):
    document = models.FileField(upload_to='static/files/')
    description = models.TextField(blank=False,null=False)
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name to be displayed on Django admin.")
    def __str__(self) -> str:
        return '{0}'.format(self.name)