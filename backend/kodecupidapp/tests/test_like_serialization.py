from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Like
from ..serializers import LikeSerializer

User = get_user_model()

class LikeSerializerTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='testpass123')
        self.user2 = User.objects.create_user(username='user2', password='testpass123')

    def test_serializer_with_valid_data(self):
        data = {
            'source_user_id': self.user1.pk,
            'target_user_id': self.user2.pk,
        }
        serializer = LikeSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        like = serializer.save()
        self.assertEqual(Like.objects.count(), 1)
        self.assertEqual(like.source_user, self.user1)
        self.assertEqual(like.target_user, self.user2)

    def test_serializer_with_invalid_data(self):
        data = {'source_user_id': 999, 'target_user_id': 998}
        serializer = LikeSerializer(data=data)
        self.assertFalse(serializer.is_valid())
