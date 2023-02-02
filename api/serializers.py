from rest_framework import serializers
from users.models import WimhElectricity

# Serializer for data table with all fields
class ElectricitySerializer(serializers.ModelSerializer):
    class Meta:
        model = WimhElectricity
        fields = '__all__'