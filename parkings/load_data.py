import json
from .models import ParkingPlace

def load():
    with open('/Users/anitakovalenko/Development/cw_parking/parkingmanager/parkings/new_rectangles.json') as f:
        data = json.load(f)

    for item in data:
        service = ParkingPlace()
        service.id = item['id']
        service.coordinates = [item['x'],item['y']]
        service.coords_add = [item['x2'],item['y2']]
        service.save()
        

def export():
    data = ParkingPlace.objects.values()
    
    formatted_data = []
    for item in data:
        formatted_item = {
            'id': item['id'],
            'x': item['coords'][0],
            'y': item['coords'][1],
            'x2': item['coords_add'][0],
            'y2': item['coords_add'][1]
        }
        formatted_data.append(formatted_item)

    with open('/Users/anitakovalenko/Development/cw_parking/parkingmanager/parkings/places.json', 'w') as f:
        json.dump(formatted_data, f, indent=4)


if __name__ == '__main__':
    load()
    export()