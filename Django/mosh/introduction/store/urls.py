from django.urls import path
from . import views

urlpatterns = [
    path(route = "products/", view=views.ProductsList.as_view(), name="all products list"),
    path('products/details/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path(route = "products-view-set/", view=views.ProductsViewSet.as_view()),
    path('products-view-set/<int:pk>/', views.ProductsViewSet.as_view()),
    path(route = "products/collection/", view=views.products_collection, name="product's collection"),
    path(route = "products/all/ordered/", view=views.ordered_products, name="all ordered products list"),
    path("products/expensive/",           views.expensive_products,   name="product price filter"), 
    path("products/statistics/", views.unit_price_stats, name="product price stats"),
    path("products/collection-stats/",views.collection_price_stats,name="collection price stats"),
    path("products/range/", views.range_of_prices, name="products in price range"),
    path("products/check/", views.expensive_low_stock, name="expensive low stock"),
    path("products/check/cheap/plenty/", views.expensive_low_stock, name="cheap high stock"),
    path("products/union/id/",views.products_union_id,name="products union id"),
    path(route = "collections/", view=views.CollectionListCreateView.as_view(), name="all products list"),
    path("collection/add/",views.new_collection,name="new collection"),
    path("collection/update/",views.update_collection,name="new collection"),
    path("order/new/",views.new_order,name="new collection"),
    path("tags/",views.tags_generic_content_type,name="tags generic")
]