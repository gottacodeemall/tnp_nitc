from django.contrib import admin
from .models import WhyUs,VisitedCompanies,Policy,ProcedureStep,PolicyFileUpload,StatsTable,ChartData,PlacementFileUpload
# Register your models here.
admin.site.register(WhyUs)
admin.site.register(VisitedCompanies)
admin.site.register(Policy)
admin.site.register(ProcedureStep)
admin.site.register(PolicyFileUpload)
admin.site.register(StatsTable)
admin.site.register(ChartData)
admin.site.register(PlacementFileUpload)