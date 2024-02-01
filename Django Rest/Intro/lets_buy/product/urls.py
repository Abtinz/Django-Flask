from django.urls import path

from product import views


urlpatterns =  [
    path("product/" , views.product_views.ser, name = "product_view")
]