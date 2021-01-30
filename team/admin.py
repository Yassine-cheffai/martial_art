from django.contrib import admin
from django.urls import reverse
from django.shortcuts import redirect
from inline_actions.admin import InlineActionsMixin
from inline_actions.admin import InlineActionsModelAdminMixin

from .models import Team, Competitor, Coach, Assistant, Participation


class CompetitorAdmin(InlineActionsMixin, admin.TabularInline):
    model = Competitor
    extra = 0
    can_delete = False

    inline_actions = ['delete']

    def delete(self, request, obj, parent_obj=None):
        obj.delete()

    delete.short_description = "Delete"


class CoachAdmin(InlineActionsMixin, admin.TabularInline):
    model = Coach
    extra = 0
    can_delete = False

    inline_actions = ['delete']

    def delete(self, request, obj, parent_obj=None):
        obj.delete()

    delete.short_description = "Delete"


class AssistantAdmin(InlineActionsMixin, admin.TabularInline):
    model = Assistant
    extra = 0
    can_delete = False

    inline_actions = ['delete']

    def delete(self, request, obj, parent_obj=None):
        obj.delete()

    delete.short_description = "Delete"


@admin.register(Team)
class TeamAdmin(InlineActionsModelAdminMixin, admin.ModelAdmin):
    inlines = [CoachAdmin, AssistantAdmin, CompetitorAdmin]


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    filter_horizontal = ['competitors']
