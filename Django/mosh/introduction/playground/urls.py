from django.urls import path
from . import views

urlpatterns = [
    path(route = "hello/", view=views.say_hello, name="hello django"),
    path(route = "products/all/", view=views.all_products, name="all products list"),
    path("products/",           views.products_by_id,   name="product detail"), 
    path(route = "hello/html/debug/", view=views.say_hello_html, name="hello django + html + debug"),

]