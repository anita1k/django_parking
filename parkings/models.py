from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class ParkingPlace(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    coordinates = ArrayField(ArrayField(models.FloatField()), blank=False)
    floor = models.IntegerField(blank=False)
    
    def __int__(self):
        return self._id
    

class Shop(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    slug = models.CharField(max_length=100) 
    coordinates = ArrayField(ArrayField(models.FloatField()), blank=False)
    category = models.CharField(max_length=100)
    floor = models.IntegerField(blank=False)
   
   
class FacilityType(models.Model):
    TYPE_CHOICES = [
        ('Elevator', 'Лифт'),
        ('Escalator', 'Эскалатор'),
        ('Entrance', 'Вход'),
    ]
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
 
    
class Facility(models.Model):
    _id = models.CharField(max_length=100, primary_key=True)
    floor = models.IntegerField(blank=False)
    coordinates = ArrayField(ArrayField(models.FloatField()), blank=False)
    slug = models.CharField(max_length=100) 
    type = models.ForeignKey(FacilityType, related_name='facilityType_set', on_delete=models.CASCADE, blank=False)
    
    

class Busy(models.Model):
    _id = models.ForeignKey(ParkingPlace, related_name='busy_set', on_delete=models.CASCADE, primary_key=True)
    is_busy = models.BooleanField()
    # created_at = models.DateTimeField(auto_now_add=True)
    

class Path(models.Model):
    _id = models.AutoField(primary_key=True)
    place_id = models.ForeignKey(ParkingPlace, related_name='path_set', on_delete=models.CASCADE, blank=False)
    shop_id = models.ForeignKey(Shop, related_name='path_set', on_delete=models.CASCADE, blank=False)
    # user_for = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    # path_coordinates = ArrayField(ArrayField(models.FloatField()), size=None)
    # path_coordinates = models.JSONField(default=list)
    path_coordinates = ArrayField(ArrayField(models.DecimalField(max_digits=10, decimal_places=2)))
    
    

    
    
# coords = ArrayField(base_field=models.FloatField(), size=2, blank=False)
