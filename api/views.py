from django.shortcuts import render
from rest_framework import viewsets
from api.models import Store, Product
from api.serializers import StoreSerializer, ProductSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        
        try:
            store = Store.objects.get(pk=pk)
            products = Product.objects.filter(store=store)
            print('Get products of store ', pk)
            
            products_serializer = ProductSerializer(products, many=True, context = {'request': request})
            
            return Response(products_serializer.data)
        except Exception as e:
            return Response({'message': 'Store does not exist'})
        
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer