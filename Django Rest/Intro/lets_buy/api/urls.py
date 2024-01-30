from django.urls import path

from api import views


urlpatterns =  [
    path("api/" , views.product_views, name = "product_view")
]