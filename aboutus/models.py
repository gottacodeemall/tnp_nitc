from django.db import models

class AboutUs(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name of the ABOUTUS ON Djanoo-admin. Do not create multiple instances.")
    aboutus = models.TextField(blank=False, null=False, help_text="HTML of About Us")
    vision=models.TextField(blank=False,null=False,help_text="HTML of Vision")
    mission=models.TextField(blank=False,null=False,help_text="HTML of Mission")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

class Academic(models.Model):
    branch=models.CharField(max_length=255, blank=False,unique=False,help_text="Name of the Branch. Eg. Computer Science and Engineering")
    subjects=models.TextField(blank=False,null=False,help_text="HTML list of core and important subjects")
    url=models.URLField()
    CHOICE = (
        ('B.Tech', 'B.Tech'),
        ('M.Tech', 'M.Tech'),
        ('MCA', 'MCA'),
    )
    stream=models.CharField(max_length=255,choices=CHOICE)
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

class New(models.Model):
    name=models.CharField(max_length=255, blank=False,unique=True,help_text="Name of the news. To be displayed on Django admin.")
    short_desc = models.CharField(max_length=255, blank=False,help_text="Short description about the news.")
    pic = models.ImageField(upload_to = 'static/img/news/', default = 'static/img/slider_3.jpg')
    alt_text = models.CharField(max_length=255, blank=False,help_text="If image does not load, this will be displayed.")
    title= models.TextField(blank=False,null=False,help_text="Title")
    content = models.TextField(blank=False,null=False,help_text="Insert content.")
    date = models.DateField(blank=False,null=False,help_text="Date of the event. Sorted based on this.")
    def __str__(self) -> str:
        return '{0}'.format(self.name)

