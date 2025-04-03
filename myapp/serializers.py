from rest_framework import serializers
from .models import Product, Customer, Order

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model."""

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            "sku": {"help_text": "Unique SKU identifier"},
            "price": {"help_text": "Price of the product in USD"},
            "stock": {"help_text": "Available stock count"},
            "source_platform": {"help_text": "Source platform (Shopify/WineDirect)"},
        }

class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer model."""

    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs = {
            "email": {"help_text": "Unique email address of the customer"},
            "source_platform": {"help_text": "Source platform (Shopify/WineDirect)"},
        }

class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order model."""

    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            "order_id": {"help_text": "Unique order identifier"},
            "source_platform": {"help_text": "Source platform (Shopify/WineDirect)"},
            "total_price": {"help_text": "Total order price in USD"},
        }
