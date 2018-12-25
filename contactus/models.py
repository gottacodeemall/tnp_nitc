from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name to be displayed on django admin. Do not create multiple instances.")
    info=models.TextField(blank=False,unique=True,help_text="html content")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

class People(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name of the person.")
    pic = models.ImageField(upload_to = 'static/img/people/', default = 'static/img/slider_3.jpg')
    alt_text = models.CharField(max_length=255, blank=False,help_text="If image does not load, this will be displayed.")
    phone=models.CharField(max_length=255, blank=False,help_text="Character field")
    email=models.CharField(max_length=255, blank=False)
    CHOICE= (
        ('Faculty', 'Faculty'),
        ('Core Committee', 'Core Committee'),
        ('Placement Representative', 'Placement Rep'),
    )
    display_in_contactus=models.BooleanField(blank=False,null=False)
    role= models.CharField(max_length=255,choices=CHOICE)
    def __str__(self) -> str:
        return '{0}'.format(self.name)




class ReachUs(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name to be displayed on Django admin. Do not create multiple instances.")
    content=models.TextField(blank=False,null=False,help_text="Enter the html content of the about us.")
    def __str__(self) -> str:
        return '{0}'.format(self.name)