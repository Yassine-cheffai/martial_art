from django.shortcuts import render
import django_tables2 as tables
from .tables import TournamentTable
from .models import Tournament
# Create your views here.


class TournmentsTableView(tables.SingleTableView):
    table_class = TournamentTable
    queryset = Tournament.objects.all()
    template_name = "tounements_list.html"