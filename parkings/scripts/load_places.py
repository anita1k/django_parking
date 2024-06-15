import json
from parkings.models import ParkingPlace


with open('/Users/anitakovalenko/Development/cw_parking/parkingmanager/parkings/new_rectangles.json') as f:
    rectangles = json.load(f)

for i, r in enumerate(rectangles, start=ParkingPlace.objects.last().id if ParkingPlace.objects.exists() else 1):
    ParkingPlace.objects.create(
        id=i,
        coords=[r.pop('x'), r.pop('y')],
        coords_add=[r.pop('x2'), r.pop('y2')]
    )