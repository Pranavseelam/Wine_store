# wine_store/urls.py

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from myapp.views import (
    ProductViewSet,
    CustomerViewSet,
    OrderViewSet,
    trigger_data_fetch,
    aggregated_metrics
)
from myapp.swagger import schema_view
from django.http import HttpResponseRedirect
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename="products")  # Maps to /api/products/
router.register(r'customers', CustomerViewSet, basename='customers')  # Maps to /api/customers/
router.register(r'orders', OrderViewSet)  # Maps to /api/orders/

# Add a simple redirect from the root URL to the API root
def redirect_to_api(request):
    return HttpResponseRedirect('/api/')

urlpatterns = [
    path('', redirect_to_api),  # Redirect root to /api/
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include all API URLs from the router

    # JWT Authentication URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get Access & Refresh Token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh Access Token

    path('api/triggersync/', trigger_data_fetch, name='trigger-sync'),  # API to sync data
    path('api/metrics/', aggregated_metrics, name='aggregated-metrics'),  # API for analytics

    # Swagger UI & ReDoc
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
