from django.core.management.base import BaseCommand
import json
from kodecupidapp.models import Tag

class Command(BaseCommand):
    help = 'Import tags from a JSON file'

    def handle(self, *args, **options):
        file_path = "kodecupidapp/management/commands/tags.json"
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item in data:
                Tag.objects.get_or_create(name=item['name'])
                
        self.stdout.write(self.style.SUCCESS('Successfully imported tags'))
