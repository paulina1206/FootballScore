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

class Season(models.Model):
    season = models.CharField(max_length=64)


