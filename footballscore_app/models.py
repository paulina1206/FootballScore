from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=64)
    flag = models.ImageField(upload_to='flags')

    def __str__(self):
        return f'{self.name}'


hierarchy_league = ((1, 'level 1'),
                    (2, 'level 2'),
                    (3, 'level 3'),
                    (4, 'level 4'))

class League(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    hierarchy = models.IntegerField(choices=hierarchy_league)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    season = models.CharField(max_length=64)

    class Meta:
        unique_together = ('hierarchy', 'country',)

    def __str__(self):
        return f'{self.name}, {self.country}'

    def get_detail_url(self):
        return f"footballscore/league/{self.id}"

class Team(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    coach = models.CharField(max_length=256)
    arms = models.ImageField(upload_to ='uploads')
    address = models.CharField(max_length=256)
    league = models.ManyToManyField(League)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

class Match(models.Model):
    team_home = models.ForeignKey(Team, related_name='match_home', on_delete=models.CASCADE)
    team_away = models.ForeignKey(Team, related_name='match_away', on_delete=models.CASCADE)
    date = models.DateField()
    score_home = models.IntegerField(default=None, null=True)
    score_away = models.IntegerField(default=None, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        if self.score_away is not None:
            if self.score_away>self.score_home:
                self.team_away.points +=3
                self.team_away.save()
            elif self.score_home>self.score_away:
                self.team_home.points +=3
                self.team_home.save()
            else:
                self.team_away.points += 1
                self.team_away.save()
                self.team_home.points += 1
                self.team_home.save()

    def __str__(self):
        return f'{self.team_home} : {self.team_away}'


    #validate -team muszą mieć tą samą ligę