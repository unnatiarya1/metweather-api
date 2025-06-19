from django.db import models

class ClimateData(models.Model):
    region = models.CharField(max_length=50)
    parameter = models.CharField(max_length=50)  # Tmax, Tmin, etc.
    year = models.IntegerField()
    month = models.IntegerField()
    value = models.FloatField()

    class Meta:
        unique_together = ('region', 'parameter', 'year', 'month')
