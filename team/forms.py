from django import forms

from .models import Team, Competitor


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"


class CompetitorForm(forms.ModelForm):
    class Meta:
        model = Competitor
        fields = "__all__"
