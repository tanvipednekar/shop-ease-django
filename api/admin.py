from django.contrib import admin
from api.models import Store, Product

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'store_id', 'description')
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'product_id', 'name', 'store_id')

# Register your models here.
admin.site.register(Store, StoreAdmin)
admin.site.register(Product, ProductAdmin)
