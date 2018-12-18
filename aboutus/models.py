from django.db import models

class CurLink(models.Model):
    branch=models.CharField(max_length=255, blank=False,unique=True,help_text="Name of the Branch. Eg. b-CSE for Btech CSE, m-CSE for Mtech")
    url=models.URLField()
    def __str__(self) -> str:
        return '{0}'.format(self.branch)

class Achievement(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name of the achievement. To be displayed on Django admin.")
    pic = models.ImageField(upload_to = 'static/img/achievements/', default = 'static/img/slider_3.jpg')
    alt_text = models.CharField(max_length=255, blank=False,help_text="If image does not load, this will be displayed.")
    title= models.TextField(blank=False,null=False,help_text="Title")
    content = models.TextField(blank=False,null=False,help_text="Insert content.")
    date = models.DateField(blank=False,null=False,help_text="Date of the event. Sorted based on this.")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

class Gallery(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name of the achievement. To be displayed on Django admin.")
    pic = models.ImageField(upload_to = 'static/img/gallery/', default = 'static/img/slider_3.jpg')
    alt_text = models.CharField(max_length=255, blank=False,help_text="If image does not load, this will be displayed.")
    info = models.TextField(blank=False,null=False,help_text="Description text of the image.")
    date = models.DateField(blank=False,null=False,help_text="Date of the event. Sorted based on this.")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

