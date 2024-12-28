from rest_framework import viewsets, generics
from .models import InventoryItem
from .serializers import InventoryItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveAPIView


class InventoryItemPagination(PageNumberPagination):
    page_size = 5


# List all items
class InventoryCreateListView(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all().order_by("date_added")
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = InventoryItemPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["category", "price"]
    ordering_fields = ["name", "quantity", "price", "date_added"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Retrieve an item
class InventoryRetrieveView(generics.RetrieveAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]


# Update Inventory Item (Update)
class InventoryUpdateView(generics.UpdateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# Delete Inventory Item (Delete)
class InventoryDeleteView(generics.DestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]
