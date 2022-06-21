from django.core.management.base import BaseCommand
from posts.models import Mountain
import csv

def boolean_converter(value):
    if value == 'TRUE':
        return True
    if value == 'FALSE':
        return False

def no_value(value):
    if value == '':
        return None
    return value


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        
        with open('data/mountain_data.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                mountain, created = Mountain.objects.get_or_create(
                    name = row['Peak'],
                    latitude = no_value(row['Latitude']),
                    longitude = no_value(row['Longitude']),
                    elevation = row['Elevation Feet'],
                    state = row['State'],
                    country = row['Country'],
                    continent = row['Continent'],
                    google_maps_url = row['Google Link'],
                    glaciated = boolean_converter(row['Glaciated Peak']),
                )
                # mountain.elevation = row['Elevation Feet']
                # mountain.save()

