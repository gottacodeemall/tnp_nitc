from django.db import models

# Create your models here.

class FooterQuicklink(models.Model):
    linkname=models.CharField(max_length=255, blank=False, null=True,unique=True,help_text="Name of the link: Eg. NITC.")
    url=models.URLField(blank=False,null=False,help_text="Name of the link: Eg. https://nitc.ac.in")
    def __str__(self) -> str:
        return '{0}'.format(self.linkname)

class FooterContactInformation(models.Model):
    classname=models.CharField(max_length=255, blank=False, null=True,help_text="Icons are provided by Icomoon and can be controlled by a class name.")
    info=models.CharField(max_length=255, blank=False, null=True,unique=True,help_text="information")
    def __str__(self) -> str:
        return '{0}'.format(self.info)

class WelcomeMessage(models.Model):
    welcomemessage=models.TextField(blank=False,null=False,help_text="Enter the html content of the welcome message.")
    def __str__(self) -> str:
        return '{0}'.format(self.welcomemessage)

class Slide(models.Model):
    number = models.PositiveIntegerField(unique=True,blank=False,null=False,help_text="slides are sorted based on this.")
    overlay_text = models.TextField(blank=False,unique=True,help_text="Text on the slide.")
    slider_pic = models.ImageField(upload_to = 'static/img/slides/', default = 'static/img/slider_3.jpg')
    def __str__(self) -> str:
        return '{0}'.format(self.overlay_text)

class LandingStat(models.Model):
    icon_class_name = models.CharField(max_length=255,blank=True,null=True,help_text="Icons are provided by Icomoon and can be controlled by a class name.")
    value = models.PositiveIntegerField(blank=False,help_text="Provide a value to be displayed.")
    speed = models.PositiveIntegerField(blank=False,help_text="Speed at which the value increases. Eg. 2000")
    labelname = models.CharField(max_length=255,blank=False,null=False,unique=True,help_text="Label to be displayed.")
    trailing_chars = models.CharField(max_length=255,blank=True,null=True,help_text="If you want 90 %add % ")
    def __str__(self) -> str:
        return '{0}'.format(self.labelname)

class FromtheTPO(models.Model):
    message=models.TextField(blank=False,null=False,help_text="Plaintext message")
    pic = models.ImageField(upload_to = 'static/img/', default = 'static/img/slider_3.jpg')
    name = models.CharField(max_length=255,blank=False,null=False,unique=True,help_text="Name of the TPO")
    def __str__(self) -> str:
        return '{0}'.format(self.name)