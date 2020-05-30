from django.db import models
from django.urls import reverse


# Create your models here.
class Teams(models.Model):
    TeamID = models.IntegerField(primary_key=True)
    TeamName = models.CharField(max_length=50)
    TeamRank = models.IntegerField()

    def get_absolute_url(self):
        return reverse('teams:details', kwargs={'teamID': self.pk})

    def __str__(self):
        return self.TeamName


class Player(models.Model):
    TeamID = models.ForeignKey(Teams, on_delete=models.CASCADE)
    PID = models.IntegerField(primary_key=True)
    PName = models.CharField(max_length=100)
    PAge = models.IntegerField()
    PType = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse('teams:index', kwargs={})

    def __str__(self):
        return self.PName
