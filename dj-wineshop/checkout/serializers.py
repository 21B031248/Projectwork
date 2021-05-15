from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "cart",
            "full_name",
            "phone_number",
            "estate",
            "address",
            "order_total",
            "checked_out",
            "active"
        )
