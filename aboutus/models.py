from django.db import models

# Create your models here.
class AboutUs(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name to be displayed on Django admin. Do not create multiple instances.")
    aboutus=models.TextField(blank=False,null=False,help_text="Enter the html content of the about us.")
    mission=models.TextField(blank=False,null=False,help_text="Enter the html content of mission.")
    vision=models.TextField(blank=False,null=False,help_text="Enter the html content of vision.")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

class Programme(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Programme opted in NITC. Eg. B.Tech")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

class Stream(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name of the stream. Eg. Computer Science and Engineering.")
    info=models.TextField(blank=False,null=False,help_text="HTML content of info and a link to the curriculum.")
    programme=models.ForeignKey(Programme,on_delete=models.CASCADE,help_text="Link it to the corresponding programme.")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

class Subject(models.Model):
    subject=models.CharField(max_length=255, blank=False,unique=True,help_text="Name of the subjects. Eg. Compiler Design.")
    stream=models.ForeignKey(Stream,on_delete=models.CASCADE,help_text="Link it to the corresponding stream")
    def __str__(self) -> str:
        return '{0}'.format(self.subject)

class Achievement(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name of the achievement. To be displayed on Django admin.")
    pic = models.ImageField(upload_to = 'static/img/slides/', default = 'static/img/slider_3.jpg')
    alt_text = models.CharField(max_length=255, blank=False,help_text="If image does not load, this will be displayed.")
    content = models.TextField(blank=False,null=False,help_text="HTML content of content.")
    date = models.DateField(blank=False,null=False,help_text="Date of the event. Sorted based on this.")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

class Gallery(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name of the achievement. To be displayed on Django admin.")
    pic = models.ImageField(upload_to = 'static/img/slides/', default = 'static/img/slider_3.jpg')
    alt_text = models.CharField(max_length=255, blank=False,help_text="If image does not load, this will be displayed.")
    info = models.TextField(blank=False,null=False,help_text="Dexription text of the image.")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

