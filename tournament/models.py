import datetime

from django.db import models
from django.core.exceptions import ValidationError


class Tournament(models.Model):
    tournament_name = models.CharField(max_length=256, null=True, blank=True)
    tournament_date = models.DateField(null=True, blank=True)
    tournament_location = models.CharField(max_length=256,
                                           null=True,
                                           blank=True)
    tournament_enrolment_close_date = models.DateTimeField()
    tournament_competition_start_date = models.DateField()
    tournament_competition_close_date = models.DateField()

    def create_competitions(self, *args, **kwargs):
        pass

    def __str__(self):
        return self.tournament_name


class Competition(models.Model):

    competitors_gender = [('Male', 'male'), ('Female', 'female')]
    competitors_category = [('Mini', 'mini'), ('Junior', 'junior'),
                            ('Cade', 'cade'), ('Senior', 'senior')]
    # this is nothing just example , we need to create a file or a data structure that can manage competitors enrolment rules
    competitors_category_weights_rules = {
        'mini': [30],
        'junior': [40],
        'cade': [60],
        'senior': [90]
    }

    tournament = models.ForeignKey(Tournament,
                                   related_name='get_competitions',
                                   on_delete=models.CASCADE,
                                   blank=True,
                                   null=True)
    competitors_gender = models.CharField(max_length=256,
                                          choices=competitors_gender)
    competitors_category = models.CharField(max_length=256,
                                            choices=competitors_category)
    competitors_weight = models.FloatField()
    competitors_years = models.CharField(max_length=512, null=True, blank=True) # a list of years seperated by comma ,  with no space, this is a wowrk arround to avoid using postgre list field

    def clean(self):
        years = [str(year) for year in range(1950, datetime.datetime.today().year)]
        for year in self.competitors_years.split(","):
            if year not in years:
                raise ValidationError("the competition years combination is not valid")

    def __str__(self):
        return f"{self.tournament.tournament_name}, {self.competitors_gender}, {self.competitors_category}, -{self.competitors_weight} KG"
