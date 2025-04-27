from django.urls import path
from . import views

urlpatterns = [
    path(route = "hello/", view=views.say_hello, name="hello django"),
    path(route = "products/all/", view=views.all_products, name="all products list"),
    path(route = "hello/html/debug/", view=views.say_hello_html, name="hello django + html + debug"),

]