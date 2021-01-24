from random import choice

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.lorem_ipsum import words
from django.views.generic.base import TemplateView
from django_filters.views import FilterView

import django_tables2 as tables
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableMixin, SingleTableView
from django_tables2.export.views import ExportMixin
from django_tables2.paginators import LazyPaginator
from .models import Tournament


class TournamentTable(tables.Table):
    class Meta:
        model = Tournament
        template_name = "django_tables2/bootstrap4.html"
        attrs = {"class": "table table-hover"}
