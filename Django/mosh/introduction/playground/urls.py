from django.urls import path
from . import views

urlpatterns = [
    path(route = "hello/", view=views.say_hello, name="hello django")
]