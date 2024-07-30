from rest_framework import serializers
from .models import Product

class  ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product
        fields = [
            'title',
            'description',
            'price',
            'get_sale_price',
            'my_discount',
        ]
    def get_my_discount(self, obj):
        #this if condition is needed when the serializer is called to save data
        #so to prevent errors of not finding an instance of that obj, because it is not created yet, we perform this check first
        if not isinstance(obj, Product):
            return None
        return obj.get_discount(float(obj.price))