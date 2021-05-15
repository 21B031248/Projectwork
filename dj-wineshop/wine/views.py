from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser

from .models import Wine
from .serializers import WineSerializer

@csrf_exempt
def wineApi(request, id=0):
    if request.method == 'GET':
        wines = Wine.objects.all()
        wine_serializer = WineSerializer(
            wines,
            many=True
        )
        return JsonResponse(wine_serializer.data, safe=False)

    elif request.method == 'POST':
        wine_data = JSONParser().parse(request)
        wine_serializer = WineSerializer(data=wine_data)
        if wine_serializer.is_valid():
            wine_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed To Add", safe=False)

    elif request.method == 'PUT':
        wine_data = JSONParser().parse(request)
        wine = Wine.objects.get(id=wine_data['id'])
        wine_seriallizer = WineSerializer(wine, data=wine_data)
        if wine_seriallizer.is_valid():
            wine_seriallizer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        wine = Wine.objects.get(id=id)
        wine.delete()
        return JsonResponse("Deleted Successfully", safe=False)
