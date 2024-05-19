from rest_framework import serializers
from api.models import Store, Product

# create serializers
class StoreSerializer(serializers.HyperlinkedModelSerializer):
    store_id = serializers.ReadOnlyField()
    class Meta:
        model = Store
        fields = '__all__'
        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    product_id = serializers.ReadOnlyField()
    class Meta:
        model = Product
        fields = "__all__"