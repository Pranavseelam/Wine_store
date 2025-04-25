# myapp/views.py

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Customer, Order
from .serializers import ProductSerializer, CustomerSerializer, OrderSerializer
from .utils import fetch_shopify_products, fetch_shopify_customers, fetch_shopify_orders

import logging

logger = logging.getLogger(__name__)

# ViewSet for Products
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        # Dynamically filter based on query parameters
        for param, value in self.request.query_params.items():
            if param in [field.name for field in Product._meta.fields]:  # Check if param exists in Product fields
                queryset = queryset.filter(**{param: value})

        return queryset

# ViewSet for Customers
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# ViewSet for Orders
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@api_view(['POST', 'GET'])
def trigger_data_fetch(request):
    """Endpoint to trigger data synchronization with Shopify"""
    try:
        logger.info("Trigger data fetch started")
        fetch_shopify_products()
        fetch_shopify_customers()
        fetch_shopify_orders()
        logger.info("Data synchronization completed")
        return Response({"status": "success", "message": "Data synchronization completed"}, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error in data fetch: {str(e)}")
        return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def aggregated_metrics(request):
    """Endpoint for aggregated metrics"""
    metrics = {
        'total_products': Product.objects.count(),
        'total_customers': Customer.objects.count(),
        'total_orders': Order.objects.count(),
        'platform_distribution': {
            'shopify_products': Product.objects.filter(source_platform='Shopify').count(),
            'winedirect_customer': Product.objects.filter(source_platform='WinDirect').count(), #if WineDirect API Access Provided
            'shopify_customers': Customer.objects.filter(source_platform='Shopify').count(),
            'winedirect_customers': Customer.objects.filter(source_platform='WineDirect').count(),#if WineDirect API Access Provided
            'shopify_orders': Order.objects.filter(source_platform='Shopify').count(),
            'winedirect_orders': Order.objects.filter(source_platform='WineDirect').count()#if WineDirect API Access Provided
        }
    }
    return Response(metrics, status=status.HTTP_200_OK)
