from rest_framework import serializers
from .models import SalesReport, InventoryTurnover

class SalesReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReport
        fields = '__all__'

class InventoryTurnoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTurnover
        fields = '__all__'
