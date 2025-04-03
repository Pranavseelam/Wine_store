import pytest
import json
from django.urls import reverse
from rest_framework.test import APIClient
from myapp.models import Product, Customer
from unittest.mock import patch

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_customer(db):
    return Customer.objects.create(first_name="John", last_name="Doe", email="john.doe@example.com", source_platform="Shopify")

@pytest.fixture
def create_product(db):  # Ensures database access
    return Product.objects.create(name="Test Wine", price=20.99, stock=10, sku="TW-001", source_platform="Shopify")

@pytest.mark.django_db
def test_get_products(api_client, create_product):
    url = reverse("products-list")  # Ensure this matches your urlpatterns name
    response = api_client.get(url)
    
    print("Response Data:", response.data)  # Debugging
    
    assert response.status_code == 200
    assert len(response.data) > 0
    assert response.data[0]["name"] == "Test Wine"

@pytest.mark.django_db
def test_create_product(api_client, db):
    url = reverse("products-list")
    data = {
        "name": "New Wine", 
        "price": 30.50, 
        "stock": 5,
        "sku": "NW-12345",  # Added required field
        "source_platform": "Shopify"  # Added required field
    }
    
    response = api_client.post(url, data, format="json")
    
    print("Response Status:", response.status_code)
    print("Response Data:", response.data)  # Debugging
    
    assert response.status_code == 201  # 201 = Created
    assert response.data["name"] == "New Wine"
    assert response.data["sku"] == "NW-12345"

@pytest.mark.django_db
def test_create_customer(api_client, db):
    url = reverse("customers-list")
    data = {
        "first_name": "Alice",
        "last_name": "Smith",
        "email": "alice.smith@example.com",
        "source_platform": "WineDirect"
    }
    
    response = api_client.post(url, data, format="json")
    
    print("Response Status:", response.status_code)
    print("Response Data:", response.data)  # Debugging
    
    assert response.status_code == 201  # 201 = Created
    assert response.data["email"] == "alice.smith@example.com"

@pytest.mark.django_db
@patch("myapp.views.fetch_shopify_products")  # ✅ Fixed mock path
@patch("myapp.views.fetch_shopify_customers")  
@patch("myapp.views.fetch_shopify_orders")  
def test_trigger_sync(mock_orders, mock_customers, mock_products, api_client):
    # ✅ Mock return values to avoid API failures
    mock_products.return_value = [{"id": 1, "title": "Test Product"}]
    mock_customers.return_value = [{"id": 1, "name": "Test Customer"}]
    mock_orders.return_value = [{"id": 1, "total_price": "100.00"}]

    url = reverse("trigger-sync")  
    response = api_client.post(url)

    # ✅ Debugging Output
    print("Response Data:", response.data)

    # ✅ Ensure mock functions were called
    mock_products.assert_called_once()
    mock_customers.assert_called_once()
    mock_orders.assert_called_once()

    # ✅ Validate response
    assert response.status_code == 200
    assert response.data["status"] == "success"
