from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer

# List all orders OR create a new one
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Save order with logged-in user
        serializer.save(user=self.request.user)


# Retrieve, Update, Delete a specific order
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

