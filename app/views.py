from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from app.models import ServiceAreas
from app.serializers import ProviderSerializer

@csrf_exempt
def providerList(request):
    if request.method == 'GET':
        providers = ServiceAreas.objects()
        serializer = ProviderSerializer(providers, many = True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ServiceAreas(data = true)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
