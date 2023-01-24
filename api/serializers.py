from rest_framework import serializers
from users.models import WimhElectricity

class ElectricitySerializer(serializers.ModelSerializer):
    class Meta:
        model = WimhElectricity
        fields = '__all__'