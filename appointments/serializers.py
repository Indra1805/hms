from rest_framework import serializers
from .models import Appointment

# create your appointments serializers here

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'