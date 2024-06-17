import json
from .models import ParkingPlace

def handle():
    with open('/Users/anitakovalenko/Development/cw_parking/parkingmanager/parkings/scripts/test.parkingplaces.json') as f:
        data = json.load(f)

    for item in data:
        service = ParkingPlace()
        service._id = item['_id']
        service.coordinates = item['coordinates']
        service.floor = item['floor']
        service.save()



if __name__ == '__main__':
    handle()
