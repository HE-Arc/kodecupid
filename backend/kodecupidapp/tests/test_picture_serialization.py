import tempfile
from PIL import Image
import os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib.auth import get_user_model
from kodecupidapp.models import Picture
from kodecupidapp.serializers import PictureSerializer
import logging

logger = logging.getLogger(__name__)

User = get_user_model()

class PictureSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        with Image.new('RGB', (100, 100)) as img:
            img.save(cls.image, 'JPEG')

        cls.test_user = User.objects.create_user(username='testuser', password='12345')

        cls.picture = Picture.objects.create(
            user=cls.test_user,
            image=SimpleUploadedFile(name='test_image.jpg', content=open(cls.image, 'rb').read(), content_type='image/jpeg')
        )

    def test_picture_serializer(self):
        """
        Test picture serializer
        """
        serializer = PictureSerializer(instance=self.picture)

        self.assertEqual(serializer.data['user'], self.test_user.id)
        self.assertTrue('image' in serializer.data)

        picture_data = {
            'user': self.test_user.id,
            'image': SimpleUploadedFile(name='new_test_image.jpg', content=open(self.image, 'rb').read(), content_type='image/jpeg')
        }
        serializer = PictureSerializer(data=picture_data)
        self.assertTrue(serializer.is_valid())
        
        new_picture = serializer.save()
        self.assertEqual(Picture.objects.count(), 2)
        self.assertEqual(new_picture.user, self.test_user)
        self.assertTrue(new_picture.image)

    @classmethod
    def tearDownClass(cls):
        logger.info(cls.image)
        super().tearDownClass()
        os.remove(cls.image)
