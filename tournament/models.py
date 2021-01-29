from django.db import models

class Tournament(models.Model):

    # user = models.ForeignKey(CustomUser,related_name='get_tournments',null=True,on_delete=models.CASCADE)

    tournament_name = models.CharField(max_length=256,null=True,blank=True)
    tournament_date = models.DateField(null=True,blank=True)
    tournament_location = models.CharField(max_length=256,null=True,blank=True)
    tournament_enrolment_close_date = models.DateTimeField()
    tournament_competition_start_date = models.DateField()
    tournament_competition_close_date = models.DateField() 

    # // TODO 
    # this can be done in two stages in models or forms 
    # add unecessary informations in forms 
    # here we add the parametres of compoetiton 
    # // TODO 
    # such as create competiton for male and female , they can be as boolean 
    # select categories that their competiton will be created 

    def create_competitions(self,*args,**kwargs):
        pass

    def __str__(self):
        return self.tournament_name



class Competition(models.Model):

    competitors_gender = [('Male','male'), ('Female','female')]
    competitors_category = [('Mini','mini'),('Junior','junior'),('Cade','cade'),('Senior','senior')]
    # this is nothing just example , we need to create a file or a data structure that can manage competitors enrolment rules
    competitors_category_weights_rules = {'mini':[30],'junior':[40],'cade':[60],'senior':[90]}


    tournament = models.ForeignKey(Tournament,related_name='get_competitions',on_delete=models.CASCADE,blank=True,null=True)
    competitors_gender = models.CharField(max_length=256,choices=competitors_gender)
    competitors_category = models.CharField(max_length=256,choices=competitors_category)
    competitors_weight = models.FloatField() 

    def __str__(self):
        return f"{self.tournament.tournament_name}, {self.competitors_gender}, {self.competitors_category}, -{self.competitors_weight} KG"
