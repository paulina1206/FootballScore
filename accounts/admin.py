from django.contrib import admin
from footballscore_app.models import Country,Match,Team,League
# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country, CountryAdmin)

class MatchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Match, MatchAdmin)

admin.site.register(Team)
admin.site.register(League)
