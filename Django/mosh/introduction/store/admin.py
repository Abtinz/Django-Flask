from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils.html import format_html, urlencode
from .models import Customer, OrderItem, Collection, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status']
    list_editable = ['unit_price']

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory > 10:
            return 'OK +'
        elif product.inventory > 0:
            return 'Low'
        return 'Out of Stock'

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']

    @admin.display(ordering="products_count")
    def products_count(self, collection):
        url = ( reverse("admin:store_product_changelist")+ "?"+ urlencode({"collection__id" :  str(collection.id)}) )

        return format_html(
            "<a href={}>{}<a>", url, collection.products_count
        )
        
    def get_queryset(self, request):
        return super().get_queryset(request)\
            .annotate(
                products_count = models.Count('product')
            )

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    search_fields = ['first_name', 'last_name', 'membership']

admin.site.register(OrderItem)