from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
import json

# Create your views here.
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    product = Product.objects.all().order_by("?").first()
    if product:
        # Assuming `get_discount` is a method that modifies the product instance
        product.get_discount(0.5)
        data = ProductSerializer(product).data
        return Response(data, status=200)
    else:
        return Response({"error": "No product found"}, status=404)