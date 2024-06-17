from .models import ParkingPlace, Shop, Facility, Busy, Path
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from .serializers import *


class ParkingPlaceViewSet(viewsets.ModelViewSet):
    queryset = ParkingPlace.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ParkingPlaceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['floor']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        floor = self.request.query_params.get('floor')
        if floor is not None:
            floor = int(floor)
            queryset = queryset.filter(floor=floor)
        return queryset
    

    
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ShopSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['floor']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        floor = self.request.query_params.get('floor')
        if floor is not None:
            floor = int(floor)
            queryset = queryset.filter(floor=floor)
        return queryset
    
    
class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FacilitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['floor']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        floor = self.request.query_params.get('floor')
        if floor is not None:
            floor = int(floor)
            queryset = queryset.filter(floor=floor)
        return queryset

    
class BusyViewSet(viewsets.ModelViewSet):
    queryset = Busy.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BusySerializer
    
    def perform_create(self, serializer):
        id = self.request.data.get('_id')
        place = ParkingPlace.objects.get(_id=id)
        serializer.save(_id=place)
        
    def perform_update(self, serializer):
        id = self.request.data.get('_id')
        place = ParkingPlace.objects.get(_id=id)
        serializer.save(_id=place)
 
    
    
class PathViewSet(viewsets.ModelViewSet):
    queryset = Path.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PathSerializer
    
 
