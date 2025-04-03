import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.urls import reverse  # Missing import

@pytest.fixture
def create_user():
    return User.objects.create_user(username="testuser", password="password123")

@pytest.mark.django_db  # Mark the test to allow database access
def test_login(api_client, create_user):
    url = reverse("token_obtain_pair")  # Ensure this is the correct URL name in your urls.py
    data = {"username": "testuser", "password": "password123"}
    response = api_client.post(url, data, format='json')  # Explicitly set format
    
    assert response.status_code == 200
    assert "access" in response.data  # Check if JWT token is returned