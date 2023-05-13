from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import ProductView, CustomerView, TransactionView

router = DefaultRouter()

router.register('customers', CustomerView, basename='customer')
router.register('products', ProductView, basename='product')
router.register('transactions', TransactionView, basename='transaction')

urlpatterns = [
    path('', include(router.urls))
]
