from django.contrib import admin
from django.urls import reverse
from django.shortcuts import redirect
from .models import Tournament, Competition
from inline_actions.admin import InlineActionsMixin
from inline_actions.admin import InlineActionsModelAdminMixin


class CompetitionAdmin(InlineActionsMixin, admin.TabularInline):
    model = Competition
    extra = 0
    inline_actions = ['apply']

    def apply(self, request, obj, parent_obj=None):
        url = reverse('admin:team_participation_add', )
        return redirect(url)

    apply.short_description = "Apply"


@admin.register(Tournament)
class TournamentAdmin(InlineActionsModelAdminMixin, admin.ModelAdmin):
    inlines = [CompetitionAdmin]
    extra = 0


admin.site.register(Competition)
