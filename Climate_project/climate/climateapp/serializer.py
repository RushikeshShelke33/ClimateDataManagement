from django.contrib.auth.models import User

from rest_framework import serializers
from .models import ClimateData


class ClimateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClimateData
        fields = ['climate', 'area_code', 'temperature', 'humidity', 'chances_of_rain']
