from django.contrib import admin
from . import models

@admin.register(models.Product)
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

admin.site.register(models.Collection)
admin.site.register(models.Customer)
admin.site.register(models.OrderItem)