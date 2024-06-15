from rest_framework import routers
from .api import *
from django.urls import path, include
from .filters import ParkingPlaceFilter


router = routers.DefaultRouter()
router.register(r'api/parking', ParkingPlaceViewSet, 'parking_places')
router.register('api/shops', ShopViewSet, 'shops')
router.register('api/facilities', FacilityViewSet, 'facilities')
router.register('api/busy', BusyViewSet, 'busy')
router.register('api/path', PathViewSet, 'path')

urlpatterns = router.urls
