import requests
from .models import Product, Customer, Order
from django.conf import settings

# Shopify API credentials from settings
SHOPIFY_ADMIN_API_ACCESS_TOKEN = settings.SHOPIFY_ADMIN_API_ACCESS_TOKEN
SHOPIFY_STORE_URL = settings.SHOPIFY_STORE_URL

HEADERS = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": SHOPIFY_ADMIN_API_ACCESS_TOKEN
}

# Function to fetch products from Shopify
def fetch_shopify_products():
    url = f"{SHOPIFY_STORE_URL}/admin/api/2023-04/products.json"

    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            products = response.json().get("products", [])
            for product in products:
                Product.objects.update_or_create(
                    sku=product["id"],  # Using product's unique ID as SKU
                    defaults={
                        "name": product["title"],
                        "price": product["variants"][0]["price"],
                        "stock": product["variants"][0]["inventory_quantity"],
                        "source_platform": "Shopify"
                    }
                )
            print(f"Successfully fetched and updated {len(products)} products.")
        else:
            print(f"Error fetching Shopify products: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching products: {str(e)}")

# Function to fetch customers from Shopify
def fetch_shopify_customers():
    url = f"{SHOPIFY_STORE_URL}/admin/api/2023-04/customers.json"

    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            customers = response.json().get("customers", [])
            for customer in customers:
                Customer.objects.update_or_create(
                    email=customer["email"],
                    defaults={
                        "first_name": customer.get("first_name", ""),
                        "last_name": customer.get("last_name", ""),
                        "source_platform": "Shopify"
                    }
                )
            print(f"Successfully fetched and updated {len(customers)} customers.")
        else:
            print(f"Error fetching Shopify customers: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching customers: {str(e)}")

# Function to fetch orders from Shopify
def fetch_shopify_orders():
    url = f"{SHOPIFY_STORE_URL}/admin/api/2023-04/orders.json"

    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            orders = response.json().get("orders", [])
            for order in orders:
                customer_data = order.get("customer", {})
                if customer_data:
                    customer, _ = Customer.objects.get_or_create(
                        email=customer_data.get("email", ""),
                        defaults={
                            "first_name": customer_data.get("first_name", ""),
                            "last_name": customer_data.get("last_name", ""),
                            "source_platform": "Shopify"
                        }
                    )
                else:
                    customer = None  # Handle orders without customer info

                # Create or update the order
                Order.objects.update_or_create(
                    order_id=order["id"],
                    defaults={
                        "customer": customer,
                        "total_price": order.get("total_price", "0.00"),
                        "created_at": order.get("created_at", ""),
                        "source_platform": "Shopify"
                    }
                )

            print(f"Successfully fetched and updated {len(orders)} orders.")
        else:
            print(f"Error fetching Shopify orders: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching orders: {str(e)}")

# Function to fetch transactions for a specific order
def fetch_order_transactions(order_id):
    url = f"{SHOPIFY_STORE_URL}/admin/api/2023-04/orders/{order_id}/transactions.json"

    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            transactions = response.json().get("transactions", [])
            print(f"Transactions for Order {order_id}: {transactions}")
            return transactions
        else:
            print(f"Error fetching transactions for Order {order_id}: {response.status_code} - {response.text}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching transactions: {str(e)}")
        return []