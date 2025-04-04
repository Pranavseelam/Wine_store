# Wine Store API

This project is a comprehensive backend API solution built with Django REST Framework, designed to streamline the management of a wine store's digital ecosystem. The primary goal is to unify and simplify the handling of product inventories, customer records, and order data through a centralized interface. Additionally, the API integrates external platforms like Shopify and WineDirect to enable seamless data synchronization, helping businesses manage both e-commerce and traditional retail operations with greater efficiency.

The motive behind this project is to bridge the gap between fragmented retail channels and provide a scalable, maintainable, and extensible backend system that supports both CRUD functionalities and real-time data analytics. It is especially useful for businesses seeking to enhance their backend infrastructure with modern RESTful practices and third-party integrations.

## Table of Contents
- [Installation](#installation)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Authentication](#authentication)
- [Usage](#usage)
- [External Integrations](#external-integrations)
- [Database](#database)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pranavseelam/Wine_store.git
   cd Wine_store
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. Set up environment variables:
   Create a `.env` file in the root directory and define the required variables:
   ```ini
   SHOPIFY_ADMIN_API_ACCESS_TOKEN=<your_shopify_api_access_token>
   SHOPIFY_API_URL=https://your-shopify-store.myshopify.com
   ```

2. Apply migrations:
   ```bash
   python manage.py migrate
   ```

3. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

Start the Django development server:
```bash
python manage.py runserver
```

The API will be available at: `http://127.0.0.1:8000/api/`

## API Documentation

The API documentation is available via Swagger:
- **SwaggerHub**: [WinecomAPI v2](https://app.swaggerhub.com/apis/helloworld135/winecomAPI/v2)
- **Local Swagger UI**: `http://127.0.0.1:8000/swagger/`
- **Local ReDoc UI**: `http://127.0.0.1:8000/redoc/`

## Authentication

This API uses JWT authentication. Obtain a token by sending a POST request to:
```bash
POST /api/token/
```
With the body:
```json
{
    "username": "yourusername",
    "password": "yourpassword"
}
```
Use the received token to authenticate requests by including it in the `Authorization` header:
```http
Authorization: Bearer <your_access_token>
```

## Usage

### Products
- **List products:** `GET /api/products/`
- **Retrieve a product:** `GET /api/products/{id}/`
- **Create a product:** `POST /api/products/`
- **Update a product:** `PUT /api/products/{id}/`
- **Delete a product:** `DELETE /api/products/{id}/`

### Customers
- **List customers:** `GET /api/customers/`
- **Retrieve a customer:** `GET /api/customers/{id}/`
- **Create a customer:** `POST /api/customers/`
- **Update a customer:** `PUT /api/customers/{id}/`
- **Delete a customer:** `DELETE /api/customers/{id}/`

### Orders
- **List orders:** `GET /api/orders/`
- **Retrieve an order:** `GET /api/orders/{id}/`
- **Create an order:** `POST /api/orders/`
- **Update an order:** `PUT /api/orders/{id}/`
- **Delete an order:** `DELETE /api/orders/{id}/`

## External Integrations

This API integrates with Shopify. To trigger a data sync with Shopify, send a request to:
```bash
POST /api/triggersync/
```

## Database

The project uses MySQL. Update your `settings.py` with the correct database credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wine_store',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License.
