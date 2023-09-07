from rest_framework import serializers
from rootApp.models import SwiftUser

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwiftUser
        fields = ('__all__')


class LogInSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwiftUser
        fields = ['username', 'password']  # Exclude 'password' field


from .models import Vehicles

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('__all__')

