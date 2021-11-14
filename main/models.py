from django.db import models


class Stat(models.Model):
    date = models.DateField()
    views = models.IntegerField(null=True, blank=True)
    clicks = models.IntegerField(null=True, blank=True)
    cost = models.FloatField()
