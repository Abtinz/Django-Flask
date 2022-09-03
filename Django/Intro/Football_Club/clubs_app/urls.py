from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('information/table' , views.clubs_table),
    path('creatnewclub' , views.new_football_club),
    path('<club_name>/information' , views.club_information)
]