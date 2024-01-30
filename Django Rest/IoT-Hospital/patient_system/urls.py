from django.urls import path
from .views import SetBedsCount, BedsCounts, AddPatient, DeletePatient, AddPatient


urlpatterns = [

    #beds and patient of hospital
    path('beds/count/add/<str:num>/', SetBedsCount),
    path('beds/count/get/', BedsCounts),
    path('patient/new/<str:name>/', AddPatient),
    path('patient/delete/<str:name>/', DeletePatient)
]