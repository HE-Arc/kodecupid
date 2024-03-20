from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from ..models import Like
from ..serializers import LikeSerializer

User = get_user_model()

class LikeSerializerTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='testpass123')
        self.user2 = User.objects.create_user(username='user2', password='testpass123')
        self.factory = RequestFactory()

    def test_serializer_with_valid_data(self):
        request = self.factory.post('/fake-url')
        request.user = self.user1

        data = {
            'target_user_id': self.user2.pk,
        }

        serializer = LikeSerializer(data=data, context={'request': request})
        
        self.assertTrue(serializer.is_valid())
        like = serializer.save()
        self.assertEqual(Like.objects.count(), 1)
        self.assertEqual(like.source_user, self.user1)
        self.assertEqual(like.target_user, self.user2)

    def test_serializer_with_invalid_data(self):
        request = self.factory.post('/another-fake-url')
        request.user = self.user1

        data = {
            # empty to simulate missing data
        }
        serializer = LikeSerializer(data=data, context={'request': request})
        self.assertFalse(serializer.is_valid())
