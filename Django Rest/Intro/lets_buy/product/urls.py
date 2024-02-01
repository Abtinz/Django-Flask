from django.urls import path

from product import views


urlpatterns =  [
    path("product/" , views.ProductViews.as_view(), name = "product_view")
]