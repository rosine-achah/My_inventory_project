from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class InventoryItem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="invemtory_item"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class InventoryChange(models.Model):
    inventory_item = models.ForeignKey(
        InventoryItem, related_name="changes", on_delete=models.CASCADE
    )
    change_quantity = models.IntegerField()
    change_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    changed_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="inventory_changes"
    )

    def __str__(self):
        return f"{self.change_type} {self.change_quantity} of {self.inventory_item.name} by {self.changed_by.username} at {self.timestamp}"
