# reports/urls.py
from django.urls import path
from .views import SalesReportView, InventoryReportView, UserReportView

urlpatterns = [
    path("sales/", SalesReportView.as_view(), name="sales-report"),
    path("inventory/", InventoryReportView.as_view(), name="inventory-report"),
    path("users/", UserReportView.as_view(), name="user-report"),
]
