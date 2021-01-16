from django.db import models
from tournament.models import Competition , Tournament

country_list = [("alg", "Algeria"),
                ("lib", "Libya"),
                ("mar", "Maroc"),
                ("tun", "Tunisia")]


class Team(models.Model):
    team_name = models.CharField(max_length=200, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    postal_code = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=False, null=False)
    country = models.CharField(max_length=200, choices=country_list)
    coach_name = models.CharField(max_length=200, blank=False, null=False)
    assistant_name = models.CharField(max_length=200, blank=True, null=True)
    telephone = models.CharField(max_length=200, blank=False, null=False)
    fax = models.CharField(max_length=200, blank=True, null=True)
    mobile_phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=False, null=False)
    website = models.CharField(max_length=200, blank=True, null=True)
    tournament = models.ForeignKey(Tournament,related_name='get_teams',on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        return self.team_name


class Competitor(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    wtf_gal = models.CharField(max_length=200, blank=False, null=False)
    sex = models.CharField(max_length=200,
                           choices=[('ml', "Male"), ("fm", "Female")])
    date_of_birth = models.DateField()
    team = models.ForeignKey(Team,related_name='get_competitors',on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition,related_name='get_competitors',on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
