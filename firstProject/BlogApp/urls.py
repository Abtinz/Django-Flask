from django.urls import path
from . import views

#address list
urlpatterns = {
    path("blog",views.firstPage)
}