from rest_framework import generics

from my_project.ecom.paginators import CustomPageNumberPagination
from .models import Product, Profile, Order
from .serializers import (
    ProductInSerializer,
    ProductOutSerializer, 
    ProfileSerializer, 
    OrderCreateSerializer, 
    OrderOutSerializer,
    ProductPriceFilterSerializer
)

# Create your views here.


class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # lookup_url_kwarg = "pk" - наименование url-параметра


class ProductListCreateAPIView(generics.ListCreateAPIView):
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductInSerializer
        return ProductOutSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        serializer = ProductPriceFilterSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)

        min_price = serializer.validated_data.get("min_price")
        max_price = serializer.validated_data.get("max_price")

        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        return queryset


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return ProductInSerializer
        return ProductOutSerializer
    

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return OrderCreateSerializer
        return OrderOutSerializer


class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return OrderCreateSerializer
        return OrderOutSerializer