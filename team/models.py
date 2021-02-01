from django.db import models
from tournament.models import Competition , Tournament
from django.contrib.auth.models import User

country_list = [("alg", "Algeria"),
                ("lib", "Libya"),
                ("mar", "Maroc"),
                ("tun", "Tunisia")]


class Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    team_name = models.CharField(max_length=200, blank=False, null=False)
    address = models.CharField(max_length=200, blank=True, null=True)
    postal_code = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, choices=country_list, blank=True, null=True)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)

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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Coach(models.Model):
    team = models.ForeignKey(Team, related_name="coachs", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Assistant(models.Model):
    team = models.ForeignKey(Team, related_name="assistants", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Participation(models.Model):
    competition = models.ForeignKey(to=Competition, on_delete=models.CASCADE)
    competitors = models.ManyToManyField(to=Competitor, related_name="participations")
    team = models.ForeignKey(to=Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team} - {self.competition}"
