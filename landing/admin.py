from django.contrib import admin
from .models import Slide,LandingStat,FromtheTPO,WelcomeMessage
admin.site.register(FromtheTPO)
admin.site.register(Slide)
admin.site.register(LandingStat)
admin.site.register(WelcomeMessage)