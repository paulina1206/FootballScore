from django.contrib import admin
from footballscore_app.models import Country, Match, Team, League, Season, TeamSeason


# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Country, CountryAdmin)

admin.site.register(League)
admin.site.register(Season)
admin.site.register(Team)
admin.site.register(TeamSeason)


class MatchAdmin(admin.ModelAdmin):
    pass


admin.site.register(Match, MatchAdmin)
