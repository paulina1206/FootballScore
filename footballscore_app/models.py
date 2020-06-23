from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'


hierarchy_league = ((1, 'level 1'),
                    (2, 'level 2'),
                    (3, 'level 3'),
                    (4, 'level 4'))


class League(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    hierarchy = models.IntegerField(unique=True, choices=hierarchy_league)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.country}'

    def get_detail_url(self):
        return f"/league/{self.id}"

class Season(models.Model):
    season = models.CharField(max_length=64)
    league = models.ManyToManyField(League)

    def __str__(self):
        return f'{self.season}'

class Team(models.Model):
    name = models.CharField(max_length=256)
    coach = models.CharField(max_length=256)
    arms = models.ImageField(upload_to ='uploads')
    address = models.CharField(max_length=256)
    season = models.ManyToManyField(Season)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

class Match(models.Model):
    team_home = models.ForeignKey(Team, related_name='match_home', on_delete=models.CASCADE)
    team_away = models.ForeignKey(Team, related_name='match_away', on_delete=models.CASCADE)
    date = models.DateField()
    score_home = models.IntegerField(default=None)
    score_away = models.IntegerField(default=None)

    def __str__(self):
        return f'{self.team_home} : {self.team_away}'