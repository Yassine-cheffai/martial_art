from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Team, Competitor
from .forms import TeamForm, CompetitorForm


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


class TeamsList(ListView):
    model = Competitor


def add_team(request):
    # form = TeamForm()
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.save()
            return redirect('teams')
    else:
        form = TeamForm()

    return render(request, 'team/add_team.html', {'form': form})


def add_competitor(request):
    if request.method == "POST":
        form = CompetitorForm(request.POST)
        if form.is_valid():
            comp = form.save(commit=False)
            comp.save()
            return redirect('teams')

    else:
        form = CompetitorForm()

    return render(request, 'team/add_comp.html', {'form': form})


# def competitor_list()
