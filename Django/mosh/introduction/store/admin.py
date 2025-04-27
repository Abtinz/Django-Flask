from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory']

admin.site.register(models.Collection)
admin.site.register(models.Customer)
admin.site.register(models.OrderItem)