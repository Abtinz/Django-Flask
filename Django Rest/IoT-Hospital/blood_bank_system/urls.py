from django.urls import path
from .views import  AddPatient, IsInCriticalMode, setBank


urlpatterns = [
    #blood bank
    path('blood/bank/set/', setBank),
    path('blood/bank/patient/add/', AddPatient),
    path('blood/bank/critical/',IsInCriticalMode)
]