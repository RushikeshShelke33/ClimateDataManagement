from django.shortcuts import render,HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from .models import ClimateData
from .serializer import ClimateDataSerializer

# Add Climate Data
class AddData(generics.CreateAPIView):
    queryset = ClimateData.objects.all()
    serializer_class = ClimateDataSerializer

# List All Climate Data
class ListData(generics.ListAPIView):
    queryset = ClimateData.objects.all()
    serializer_class = ClimateDataSerializer

# List Climate Data by Area
class ListDataByArea(generics.ListAPIView):
    serializer_class = ClimateDataSerializer

    def get_queryset(self):
        area_code = self.kwargs['area_code']
        return ClimateData.objects.filter(area_code=area_code)

# List Climate Data by Area and Climate
class ListDataByAreaAndClimate(generics.ListAPIView):
    serializer_class = ClimateDataSerializer

    def get_queryset(self):
        area_code = self.kwargs['area_code']
        climate = self.kwargs['climate']
        return ClimateData.objects.filter(area_code=area_code, climate=climate)

class ClimateDeltaView(generics.CreateAPIView):
    serializer_class = ClimateDataSerializer

    def create(self, request, *args, **kwargs):
        from_climate = request.data.get('from_climate')
        to_climate = request.data.get('to_climate')
        area_code = request.data.get('area_code')

        # Check if area code exists
        if not ClimateData.objects.filter(area_code=area_code).exists():
            return Response({"error": "Area code does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if climates exist
        if not ClimateData.objects.filter(area_code=area_code, climate=from_climate).exists() or \
                not ClimateData.objects.filter(area_code=area_code, climate=to_climate).exists():
            return Response({"error": "Climate data not found for specified area and climate."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Calculate climate deltas and climate change index (implement this logic)
        climate_delta = f"{from_climate} -> {to_climate}"
        temperature_delta = 0  # Calculate based on your data
        humidity_delta = 0  # Calculate based on your data
        rain_chances_delta = 0  # Calculate based on your data
        climate_change_index = 0  # Calculate based on your data

        response_data = {
            "climate_delta": climate_delta,
            "temperature_delta": temperature_delta,
            "humidity_delta": humidity_delta,
            "rain_chances_delta": rain_chances_delta,
            "climate_change_index": climate_change_index
        }

        return Response({"success": True, "data": response_data}, status=status.HTTP_200_OK)

def home(request):
    return HttpResponse("<h1> Django Climate App Intern Assignment</h1>")
