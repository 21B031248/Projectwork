from rest_framework import serializers
from .models import *

class CartSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ("id", "wines", "checked_out", "total")

class CartItemserializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ("id", "cart", "quantity", "wine", "total")
