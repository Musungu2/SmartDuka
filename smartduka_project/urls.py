from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to SmartDuka API")


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path("users/", include("users.urls")),
    path("inventory/", include("inventory.urls")),
    path("orders/", include("orders.urls")),
    path("reports/", include("reports.urls")),
]

