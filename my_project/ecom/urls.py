from django.urls import path
from .views import (
    ProfileListCreateAPIView, 
    ProfileRetrieveUpdateDestroyAPIView, 
    ProductRetrieveUpdateDestroyAPIView, 
    ProductListCreateAPIView,
    OrderListCreateAPIView,
    OrderRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # Profile
    path("profiles/", ProfileListCreateAPIView.as_view(), name="profile-list-create"),
    path("profiles/<int:pk>", ProfileRetrieveUpdateDestroyAPIView.as_view(), name="profile-detail"),

    # Product
    path("products/", ProductListCreateAPIView.as_view(), name="product-list-create"),
    path("products/<int:pk>", ProductRetrieveUpdateDestroyAPIView.as_view(), name="product-detail"),

    # Order
    path("orders/", OrderListCreateAPIView.as_view(), name="order-list-create"),
    path("orders/<int:pk>", OrderRetrieveUpdateDestroyAPIView.as_view(), name="order-detail")
]