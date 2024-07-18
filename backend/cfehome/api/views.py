from django.http import JsonResponse
from products.models import Product
from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

# Create your views here.
@api_view(["GET "])
def api_home(request, *args, **kwargs):
    product = Product.objects.all().order_by("?").first()
    if product:
        data = model_to_dict(product, fields=["title", "description"])
    return Response(data, status=200, content_type="Application/json")