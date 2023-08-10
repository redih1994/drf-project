from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductsSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk' #default



class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk' #default