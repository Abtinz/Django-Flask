from pprint import pprint
from django.urls import path, include
from rest_framework_nested import routers
from . import views

#routers are being defined aim to control view set class which we've implemented for products view
router = routers.DefaultRouter()
router.register('products-view-set', views.ProductsViewSet)
router.register('carts', views.CartView)
router.register('customers', views.CustomerViewSet)

#nested model views urls ...
product_router = routers.NestedDefaultRouter(router, 'products-view-set', lookup="product")
product_router.register('reviews', views.ReviewsDetailView, basename='product-reviews')
pprint(router.urls)
pprint(product_router.urls)



urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path(route = "products/", view=views.ProductsList.as_view(), name="all products list"),
    path(route ='products/details/<int:pk>/', view = views.ProductDetail.as_view(), name='product-detail'),
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