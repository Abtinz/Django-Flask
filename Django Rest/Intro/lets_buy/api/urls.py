

from django.urls import path

from api import views


urlpatterns =  [
    path("/product" , views.product_views, name = "product_view")
]