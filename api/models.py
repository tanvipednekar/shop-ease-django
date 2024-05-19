from django.db import models

# Create your models here.

class Store(models.Model):
    
    STORE_TYPES = (
        ('TECH', 'Technology'),
        ('FASHION', 'Fashion'),
        ('FOOD', 'Food & Beverages'),
        ('BOOK', 'Books & Stationery'),
        ('SPORT', 'Sports & Outdoors'),
    )
    
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    type = models.CharField(max_length=30, choices=STORE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

