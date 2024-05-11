from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, PurchaseOrderViewSet,VendorPerformanceViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'vendors', VendorViewSet, basename='vendor')
router.register(r'purchase_orders', PurchaseOrderViewSet, basename='purchaseorder')
router.register(r'performance',VendorPerformanceViewSet,basename='vendorperformance')

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls
