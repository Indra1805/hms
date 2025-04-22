from rest_framework import serializers
from .models import Appointment

class AppointmentValidator(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        exclude = ['appointment_id', 'billing', 'created_at']
