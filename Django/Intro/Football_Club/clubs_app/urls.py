from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('information/table' , views.clubes_table),
    path('<club_name>/information' , views.clube_information)
]