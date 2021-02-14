from django import forms
from django.core.exceptions import ValidationError

from .models import Participation


class ParticipationForm(forms.ModelForm):
    model = Participation

    def clean(self):
        competitors = self.cleaned_data.get("competitors")
        competition = self.cleaned_data.get("competition")

        if not competitors:
            raise ValidationError("you should select competitors")

        for competitor in competitors:
            if competitor.weight > competition.competitors_weight:
                raise ValidationError("competitor weight surpass the competition max weight")

        self._validate_unique = True
        return self.cleaned_data
