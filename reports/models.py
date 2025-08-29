from django.db import models
from django.conf import settings

class Report(models.Model):
    REPORT_TYPES = [
        ("sales", "Sales Report"),
        ("inventory", "Inventory Report"),
        ("user", "User Activity Report"),
    ]

    name = models.CharField(max_length=100)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    generated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="reports/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.report_type})"
