from django.contrib import admin
from .models import Tournament, Competition


class CompetitionAdmin(admin.TabularInline):
    model = Competition


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    inlines = [CompetitionAdmin]


admin.site.register(Competition)
