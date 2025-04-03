from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    stock = models.IntegerField()  # Rename 'stock' to 'inventory_count'
    source_platform = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    source_platform = models.CharField(max_length=50)  # Shopify or WineDirect

    def __str__(self):
        return self.email

class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True)  # Shopify Order ID
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.FloatField()
    created_at = models.DateTimeField()
    source_platform = models.CharField(max_length=50, default="Shopify")

    def __str__(self):
        return f"Order {self.order_id} - {self.customer.email}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"