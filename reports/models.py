from django.db import models
from inventory.models import Product

class SalesReport(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    total_sales = models.DecimalField(max_digits=12, decimal_places=2)
    top_selling_products = models.TextField()

class InventoryTurnover(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    times_sold = models.PositiveIntegerField()
    period_start = models.DateField()
    period_end = models.DateField()

