from django.urls import path
from . import views

#address list
urlpatterns = {
    path("",views.home) ,
    path("contact",views.contact),
    path("profile/<username>",views.account),
}