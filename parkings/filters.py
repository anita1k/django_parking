import django_filters
from .models import ParkingPlace


class ParkingPlaceFilter(django_filters.FilterSet):
    floor = django_filters.NumberFilter(lookup_expr='exact')
    
    class Meta:
        model = ParkingPlace
        fields = ['floor']
        