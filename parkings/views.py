import json
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser 
from rest_framework import status

from django.http import HttpResponse
from .models import ParkingPlace, Shop, Facility, Busy, Path
from .serializers import *
from django.http.response import JsonResponse


class ParkingPlaceView(APIView):
    def get(self, request):
        floor = request.GET.get('floor')
        if floor:
            try:
                floor = int(floor)
                parkings = ParkingPlace.objects.filter(floor=floor)
                if not parkings:
                    return Response({'error': 'No parking spaces found on this floor'}, status=404)
            except ValueError:
                return Response({'error': 'Invalid floor value'}, status=400)
        else:
            parkings = ParkingPlace.objects.all()
        serializer = ParkingPlaceSerializer(parkings, many=True)
        return Response(serializer.data)
    
    @method_decorator(api_view(['POST']))
    def post(self, request):
        place_data = JSONParser().parse(request)
        place_serializer = ParkingPlaceSerializer(data=place_data)
        if place_serializer.is_valid():
            place_serializer.save()
            return JsonResponse(place_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(place_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ShopView(APIView):
    @method_decorator(api_view(['GET']))
    def get(self):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)
    
    @method_decorator(api_view(['POST']))
    def post(self, request):
        shop_data = JSONParser().parse(request)
        shop_serializer = ShopSerializer(data=shop_data)
        if shop_serializer.is_valid():
            shop_serializer.save()
            return JsonResponse(shop_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(shop_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FacilityView(APIView):
    @method_decorator(api_view(['GET']))
    def get(self):
        facilities = Facility.objects.all()
        serializer = FacilitySerializer(facilities, many=True)
        return Response(serializer.data)
    
    @method_decorator(api_view(['POST']))
    def post(self, request):
        facility_data = JSONParser().parse(request)
        facility_serializer = FacilitySerializer(data=facility_data)
        if facility_serializer.is_valid():
            facility_serializer.save()
            return JsonResponse(facility_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(facility_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BusyView(APIView):    
    @method_decorator(api_view(['GET']))
    def get(self):
        busy = Busy.objects.all()
        serializer = BusySerializer(busy, many=True)
        return Response(serializer.data)
    
    @method_decorator(api_view(['POST']))
    def post(self, request):
        busy_data = JSONParser().parse(request)
        busy_serializer = BusySerializer(data=busy_data)
        if busy_serializer.is_valid():
            busy_serializer.save()
            return JsonResponse(busy_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(busy_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @method_decorator(api_view(['PATCH']))
    def patch(self, request, pk):
        try:
            busy = Busy.objects.get(id=pk)
            busy.is_busy = request.data['is_busy']
            busy.save()
            return Response(status=status.HTTP_200_OK)
        except Busy.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



class PathView(APIView):
    @method_decorator(api_view(['GET']))
    def get(self, request):
        path = Path.objects.all()
        serializer = PathSerializer(path, many=True)
        return Response(serializer.data)
    
    @method_decorator(api_view(['POST']))
    def post(self, request):
        path_data = JSONParser().parse(request)
        path_serializer = PathSerializer(data=path_data)
        if path_serializer.is_valid():
            path_serializer.save()
            return JsonResponse(path_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(path_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def home(request):
#     places = ParkingPlace.objects.all()
#     # places_id = list()
    
#     # for place in places:
#     #     places_id.append(str(place.id))
        
#     # response_html = '<br>'.join(places_id)
#     return render(request, 'home.html', {'places': places}) 
