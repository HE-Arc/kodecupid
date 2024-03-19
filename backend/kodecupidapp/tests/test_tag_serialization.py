from django.test import TestCase
from kodecupidapp.models import Tag
from kodecupidapp.serializers import TagSerializer

class TagSerializerTest(TestCase):
    def setUp(self):
        self.tag_name = 'C++'
        self.tag = Tag.objects.create(name=self.tag_name)

    def test_tag_serializer(self):
        serialized_tag = TagSerializer(instance=self.tag).data
        self.assertEqual(serialized_tag['name'], self.tag_name)
