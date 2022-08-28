from rest_framework import serializers
from .models import RationFarm

class RationFarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = RationFarm
        fields = '__all__' 