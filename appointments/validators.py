from rest_framework import serializers
from .models import Appointment
from patients import models

# create your appointments validators here

class AppointmentValidator(serializers.Serializer):
    patient_name = serializers.CharField()
    doctor_name = serializers.CharField()
    date = serializers.DateField()
    time = serializers.TimeField()
    age = serializers.IntegerField()
    appointment_type = serializers.ChoiceField(choices=Appointment.AppointmentStatus.choices)
    notes = serializers.CharField(required=False, allow_blank=True)
    gender = serializers.ChoiceField(choices=Appointment.GenderStatus.choices)
    phno = serializers.CharField()
    email = serializers.EmailField()
    blood_group = serializers.ChoiceField(choices=Appointment.BloodGroupChoices.choices, required=False)
    billing = serializers.PrimaryKeyRelatedField(queryset=models.Invoice.objects.all(), required=False)
    ward_no = serializers.CharField(required=False, allow_blank=True)
    diagnosis = serializers.CharField(required=False, allow_blank=True)