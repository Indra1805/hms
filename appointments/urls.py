from django.urls import path
from .views import *

# create your appointments requests here

urlpatterns =[
    path('get-appointments/<str:appointment_id>/',AppointmentRetrieveAPIView.as_view(),name='get-appointments'),
    path('get-appointments-list/',AppointmentListAPIView.as_view(),name='get-appointments-list'),
    path('create-appointments/',AppointmentCreateAPIView.as_view(),name='create-appointments'),
]