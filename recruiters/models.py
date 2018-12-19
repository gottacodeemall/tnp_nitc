from django.db import models

# Create your models here.
class WhyUs(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name to be displayed on Django admin. Do not create multiple instances.")
    content=models.TextField(blank=False,null=False,help_text="Enter the html content of WhyUs")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

class VisitedCompanies(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Company Name")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

class Policy(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name to be displayed on Django admin. Do not create multiple instances.")
    content=models.TextField(blank=False,null=False,help_text="Enter the html content of Policies.")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

class ProcedureStep(models.Model):
    number=models.PositiveIntegerField(unique=True,blank=False,null=False,help_text="Step number.")
    content=models.TextField(blank=False,null=False,help_text="Enter the html content of Step.")
    def __str__(self) -> str:
        return '{0}'.format(self.number)

class PolicyFileUpload(models.Model):
    document = models.FileField(upload_to='static/files/policy/')
    description = models.TextField(blank=False,null=False)
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name to be displayed on Django admin.")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

class StatsTable(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name of the table. Eg. Place Stats 2018")
    content=models.TextField(blank=False,null=False,help_text="HTML content of the table. Make it responsive.")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

class ChartData(models.Model):
    charttype=models.CharField(max_length=255, blank=False,help_text="Eg. bar ")
    chartlabel=models.CharField(max_length=255, blank=False,unique=True,help_text="Eg. Avg Package")
    labels=models.TextField(blank=False,null=False,help_text="Enter the labels seperated by commas without spaces after and before comma Eg. (2010,2011,2012) or (cse,ece,eee) or (c s e,e c e,e e e)")
    data=models.TextField(blank=False,null=False,help_text="Enter the data seperated by commas without spaces after and before comma Eg. (110,111,230)")
    def __str__(self) -> str:
        return '{0}'.format(self.chartlabel)

class PlacementFileUpload(models.Model):
    document = models.FileField(upload_to='static/files/statistics/')
    description = models.TextField(blank=False,null=False)
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name to be displayed on Django admin.")
    def __str__(self) -> str:
        return '{0}'.format(self.name)