# Unified Wine & E-commerce Data API

## Overview

This API aggregates product, customer, and order data from Shopify and (if available) WineDirect. It provides endpoints to manage products and customers while offering analytics on the imported data. The API is built using Django and Django REST Framework (DRF) with JWT authentication.

## Features

- Fetch product, customer, and order data from Shopify
- Store and manage imported data in a MySQL or MongoDB database
- Provide API endpoints for products and customers
- Authentication using JWT tokens
- Real-time metrics and analytics
- OpenAPI documentation via Swagger and ReDoc

---

## Prerequisites

Ensure you have the following installed:

- **Python 3.10+**
- **Git**
- **Django**
- **Django REST Framework**
- **MySQL or MongoDB (whichever you configured) {MySQL is the DB used during the devolopment}**
- **Shopify API Credentials**
- **Postman or cURL (for API testing)**
- **GitHub Desktop (optional, for GUI-based git management)**

---

## Setup Instructions

### 1. Clone the Repository

```sh
# Clone the repository from GitHub
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create a Virtual Environment & Install Dependencies

```sh
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a **.env** file in the project root and add your credentials:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=localhost  # or your DB host
DATABASE_PORT=3306  # MySQL default port
SHOPIFY_API_KEY=your_shopify_api_key
SHOPIFY_API_SECRET=your_shopify_api_secret
```

### 4. Apply Migrations & Create Superuser

```sh
# Apply migrations
python manage.py migrate

# Create a superuser (follow the prompts)
python manage.py createsuperuser
```

### 5. Run the Django Development Server

```sh
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`.

---

## API Endpoints & Usage

### **1. Authentication (JWT)**

#### **Obtain Access & Refresh Token**

```sh
POST /api/token/
```

Example request:

```json
{
  "username": "admin",
  "password": "yourpassword"
}
```

#### **Refresh Token**

```sh
POST /api/token/refresh/
```

### **2. Product API**

#### **Retrieve All Products**

```sh
GET /api/products/
```

#### **Retrieve a Single Product**

```sh
GET /api/products/{id}/
```

#### **Create a New Product**

```sh
POST /api/products/
```

Example Payload:

```json
{
  "name": "Red Wine",
  "price": 50.00,
  "stock": 100
}
```

### **3. Customer API**

#### **Retrieve All Customers**

```sh
GET /api/customers/
```

#### **Retrieve a Single Customer**

```sh
GET /api/customers/{id}/
```

#### **Create a New Customer**

```sh
POST /api/customers/
```

Example Payload:

```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

### **4. Data Synchronization API**

#### **Trigger Shopify Data Fetch**

```sh
POST /api/triggersync/
```

### **5. Aggregated Metrics API**

#### **Retrieve Metrics**

```sh
GET /api/metrics/
```

Example Response:

```json
{
  "total_products": 120,
  "total_customers": 300,
  "total_orders": 500
}
```

---

## API Documentation

The API is documented using **Swagger** and **ReDoc**.

- **Swagger UI:** [`http://127.0.0.1:8000/swagger/`](http://127.0.0.1:8000/swagger/)
- **ReDoc:** [`http://127.0.0.1:8000/redoc/`](http://127.0.0.1:8000/redoc/)

---

## Deployment

### **Deploying to a Cloud Server (e.g., AWS, DigitalOcean)**

1. Set up a cloud VM (Ubuntu recommended).
2. Install dependencies (`Python`, `pip`, `Django`, `MySQL`).
3. Clone the repository and configure `.env`.
4. Set up **Gunicorn** and **Nginx** for production.
5. Use **Docker** or **Docker Compose** for containerized deployment.

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Your message"`).
4. Push to your fork (`git push origin feature-branch`).
5. Open a **Pull Request**.

---

## License

This project is licensed under the **MIT License**.

---

## Contact

For any issues, open a GitHub **Issue** or contact `your.email@example.com`.

---

### 🎉 Happy Coding! 🚀

