import json
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductsSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").last()
    data = {}
    if instance:
        data = ProductsSerializer(instance).data
    return Response(data)
