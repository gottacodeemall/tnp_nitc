from django.contrib import admin
from .models import FooterQuicklink,FooterContactInformation,Slide,LandingStat,FromtheTPO
# Register your models here.
admin.site.register(FromtheTPO)
admin.site.register(FooterQuicklink)
admin.site.register(FooterContactInformation)
admin.site.register(Slide)
admin.site.register(LandingStat)