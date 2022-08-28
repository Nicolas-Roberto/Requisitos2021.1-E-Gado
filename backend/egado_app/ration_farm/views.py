from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import RationFarm
from .serializers import RationFarmSerializer

class RationFarmListAPIView(ListCreateAPIView):
    serializer_class = RationFarmSerializer
    queryset = RationFarm.objects.all()

    def perform_create(self, serializer):
        return serializer.save()
    
class RationFarmDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RationFarmSerializer
    queryset = RationFarm.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        return serializer.save()