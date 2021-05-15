from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser

from .models import *
from .serializer import CartSerialzer, CartItemserializer

@csrf_exempt
def cartApi(request, id=0):
    if request.method == 'GET':
        cart = Cart.objects.get_cart(request)
        cart_serializer = CartSerialzer(
            cart
        )
        return JsonResponse(cart_serializer.data, safe=False)

    elif request.method == 'POST':
        cart_data = JSONParser().parse(request)
        cart_serializer = CartSerialzer(data=cart_data)
        if cart_serializer.is_valid():
            cart_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed To Add", safe=False)

    elif request.method == 'PUT':
        cart_data = JSONParser().parse(request)
        cart = Cart.objects.get(id=cart_data['id'])
        cart_seriallizer = CartSerialzer(cart, data=cart_data)
        if cart_seriallizer.is_valid():
            cart_seriallizer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

@csrf_exempt
def cartItemApi(request, id=0):
    if request.method == 'GET':
        cart = Cart.objects.get_cart(request)
        cart_items = CartItem.objects.filter(cart=cart)
        cart_item_serializer = CartItemserializer(
            cart_items,
            many=True
        )
        return JsonResponse(cart_item_serializer.data, safe=False)

    elif request.method == 'POST':
        cart_item_data = JSONParser().parse(request)
        cart_item_serializer = CartItemserializer(data=cart_item_data)
        if cart_item_serializer.is_valid():
            cart_item_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed To Add", safe=False)

    elif request.method == 'PUT':
        cart_item_data = JSONParser().parse(request)
        cart_item = CartItem.objects.get(id=cart_item_data['id'])
        cart_item_seriallizer = CartItemserializer(cart_item, data=cart_item_data)
        if cart_item_seriallizer.is_valid():
            cart_item_seriallizer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        cart_item = CartItem.objects.get(id=id)
        cart_item.delete()
        return JsonResponse("Deleted Successfully", safe=False)
