from rest_framework import serializers
from  .models import *

class  ParkingPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ParkingPlace
        fields = '__all__'
        
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        
class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'
        
class BusySerializer(serializers.ModelSerializer):
    class Meta:
        model = Busy
        fields = '__all__'

class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = '__all__'
