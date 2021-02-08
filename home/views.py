from django.shortcuts import render
from tournament.models import Tournament


def home(request):
    tournaments = Tournament.objects.all()
    return render(request, "home/index.html", context={"tournaments": tournaments})
