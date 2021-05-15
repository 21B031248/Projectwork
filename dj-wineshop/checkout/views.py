from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser

from .models import *
from .serializers import OrderSerializer

@csrf_exempt
def orderApi(request, id=0):
    if request.method == 'GET':
        order = Order.objects.all()
        order_serializer = OrderSerializer(
            order,
            many=True
        )
        return JsonResponse(order_serializer.data, safe=False)

    elif request.method == 'POST':
        order_data = JSONParser().parse(request)
        order_serializer = OrderSerializer(data=order_data)
        if order_serializer.is_valid():
            order_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed To Add", safe=False)
