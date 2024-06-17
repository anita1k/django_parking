import json
from .models import ParkingPlace, Shop, Facility

def parkingplace():
    with open('data/test.parkingplaces.json') as f:
        data = json.load(f)

    for item in data:
        service = ParkingPlace()
        service._id = item['_id']
        service.coordinates = item['coordinates']
        service.floor = item['floor']
        service.save()


def shop():
    with open('data/test.shops.json') as f:
        data = json.load(f)

    for item in data:
        service = Shop()
        service._id = item['_id']
        service.slug = item.get('slug', 'default_slug')
        service.coordinates = item['coordinates']
        service.category = item.get('category', 'default_category')
        service.floor = item['floor']
        service.save()


def facility():
    with open('data/test.facilities.json') as f:
        data = json.load(f)

    for item in data:
        service = Facility()
        service._id = item['_id']
        service.floor = item['floor']
        service.coordinates = item['coordinates']
        service.slug = item.get('slug', 'default_slug')
        service.type = item['type']
        service.save()


if __name__ == '__main__':
    parkingplace()
    shop()
    facility()
