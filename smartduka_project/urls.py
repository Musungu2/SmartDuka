from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to SmartDuka API")


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home, name="home"),

    # Accounts / Authentication routes
    path("users/", include("users.urls")),

    # Inventory routes
    path("inventory/", include("inventory.urls")),

    # Orders routes
    path("orders/", include("orders.urls")),

    # Reports routes
    path("reports/", include("reports.urls")),
]

