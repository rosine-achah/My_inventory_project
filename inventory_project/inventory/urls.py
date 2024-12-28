from django.urls import path, include

# from rest_framework.routers import DefaultRouter

# from .views import InventoryItemViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    InventoryCreateListView,
    InventoryRetrieveView,
    InventoryUpdateView,
    InventoryDeleteView,
)

# router = DefaultRouter()
# router.register(r"inventory", InventoryRetrieveView)


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("", include(router.urls)),
    # path("/inventory/items/<id>/", InventoryItemViewSet.as_view(), name="create"),
    # path("inventory/", InventoryCreateListView.as_view(), name="inventory-list"),
    # path(
    #     "inventory/<int:pk>/",
    #     InventoryItemDetailView.as_view(),
    #     name="inventory-detail",
    # ),
    path("inventory/", InventoryCreateListView.as_view(), name="inventory-list-create"),
    path(
        "inventory/<int:pk>/",
        InventoryRetrieveView.as_view(),
        name="inventory-retrieve",
    ),
    path(
        "inventory/<int:pk>/update/",
        InventoryUpdateView.as_view(),
        name="inventory-update",
    ),
    path(
        "inventory/<int:pk>/delete/",
        InventoryDeleteView.as_view(),
        name="inventory-delete",
    ),
    path("api/token/", include("rest_framework_simplejwt.urls")),
]
