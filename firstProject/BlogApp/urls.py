from django.urls import path
from . import views

#address list
urlpatterns = {
    path("home",views.firstPage) ,
    path("contact",views.contact)
}