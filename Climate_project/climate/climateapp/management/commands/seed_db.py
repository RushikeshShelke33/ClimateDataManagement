from django.core.management.base import BaseCommand
from climateapp.models import ClimateData
import random

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):
        climates = ['hot', 'humid', 'rainy', 'cold']
        area_codes = range(100, 130)  # 30 area codes from 100 to 129

        for area_code in area_codes:
            for climate in climates:
                temperature = random.uniform(0, 50)  # Random temperature between 0 and 50
                humidity = random.uniform(0, 100)  # Random humidity between 0 and 100
                chances_of_rain = random.uniform(0, 100)  # Random chances of rain between 0 and 100

                ClimateData.objects.create(
                    climate=climate,
                    area_code=area_code,
                    temperature=temperature,
                    humidity=humidity,
                    chances_of_rain=chances_of_rain
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))
