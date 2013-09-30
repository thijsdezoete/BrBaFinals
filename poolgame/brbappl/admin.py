from models import People, Contestant, Result
from django.contrib import admin


class PeopleAdmin(admin.ModelAdmin):
    pass

    # search_fields = ("cdn","percentile","ts")
    # list_display = ("cdn","percentile","performance","sample_date")

# class PerformanceCountryAdmin(admin.ModelAdmin):
#   search_fields = ("cdn",'country')
#   list_display = ("cdn","country","percentile","performance","sample_date")   

admin.site.register(Contestant)
admin.site.register(Result)
admin.site.register(People, PeopleAdmin)

# admin.site.register(CdnAvailability)
# admin.site.register(CdnAvailabilityCountry)