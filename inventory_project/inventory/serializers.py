from rest_framework import serializers
from .models import InventoryItem
from .models import InventoryChange


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = [
            "id",
            "name",
            "description",
            "quantity",
            "price",
            "category",
            "date_added",
            "last_updated",
        ]


class InventoryChange(serializers.ModelSerializer):
    inventory_item = serializers.StringRelatedField()
    inventory_item_id = serializers.PrimaryKeyRelatedField(
        queryset=InventoryItem.objects.all(), write_only=True, source=inventory_item
    )
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = InventoryChange
        fields = [
            "id",
            "inventory_item",
            "inventory_item_id",
            "change_quantity",
            "change_type",
            "timestamp",
            "changed_by",
        ]
