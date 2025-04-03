from django.contrib import admin
from .models import Product, Customer, Order

try:
    from .models import OrderItem
    admin.site.register(OrderItem)
except ImportError:
    print("OrderItem model not found, skipping admin registration.")

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)