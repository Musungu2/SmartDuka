from rest_framework import generics, views
from rest_framework.response import Response
from django.db.models import Sum, Count
from orders.models import Order, OrderItem
from inventory.models import Product
from django.conf import settings

class SalesReportView(views.APIView):
    def get(self, request):
        sales_data = (
            Order.objects.values("created_at__date")
            .annotate(total_sales=Sum("total_amount"))
            .order_by("created_at__date")
        )
        return Response(sales_data)

class InventoryReportView(views.APIView):
    def get(self, request):
        low_stock = Inventory.objects.filter(quantity__lt=10).values("name", "quantity")
        return Response(low_stock)

class UserReportView(views.APIView):
    def get(self, request):
        users_count = User.objects.count()
        recent_users = User.objects.order_by("-date_joined")[:5].values("username", "date_joined")
        return Response({
            "total_users": users_count,
            "recent_users": list(recent_users)
        })

