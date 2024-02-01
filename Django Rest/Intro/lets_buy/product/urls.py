from django.urls import path

from product import views


urlpatterns =  [
    path("product/" , views.ProductViews.as_view(), name = "product_view"),
    path("product/<id>/" , views.SingleProductViews.as_view(), name = "single_product_view")
]