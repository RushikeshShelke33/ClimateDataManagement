from django.db import models
from django.contrib.auth.models import User



class ClimateData(models.Model):
    CLIMATE_CHOICES = [
        ('hot', 'Hot'),
        ('humid', 'Humid'),
        ('rainy', 'Rainy'),
        ('cold', 'Cold'),
    ]

    climate = models.CharField(max_length=5, choices=CLIMATE_CHOICES)
    area_code = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    chances_of_rain = models.FloatField()

    def __str__(self):
        return f'{self.climate} in area {self.area_code}'
