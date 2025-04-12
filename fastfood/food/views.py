from rest_framework import generics
from .models import Category, Product, Client, Order
from .serializers import CategorySerializer, ProductSerializer, ClientSerializer, OrderSerializer
from .permissions import IsAdminCreateReadDeleteOnly, IsClientReadOnly, IsClientCreateReadOnly
from .throttles import CategoryThrottle, ProductThrottle, ClientThrottle, OrderThrottle


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminCreateReadDeleteOnly]
    throttle_classes = [CategoryThrottle]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminCreateReadDeleteOnly]
    throttle_classes = [CategoryThrottle]


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminCreateReadDeleteOnly]
    throttle_classes = [ProductThrottle]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminCreateReadDeleteOnly]
    throttle_classes = [ProductThrottle]


class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsClientReadOnly]
    throttle_classes = [ClientThrottle]


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsClientReadOnly]
    throttle_classes = [ClientThrottle]


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsClientCreateReadOnly]
    throttle_classes = [OrderThrottle]


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsClientCreateReadOnly]
    throttle_classes = [OrderThrottle]
