from django.contrib import admin
from .models import Appointment

# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id','appointment_id','patient','patient_name','doctor_name','date','time','age','appointment_type','notes','gender','phno','email','blood_group','billing','ward_no','diagnosis','created_at']