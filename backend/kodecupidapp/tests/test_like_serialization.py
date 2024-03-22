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


    def test_match_detection(self):

        # User1 likes User2
        request_user1_likes_user2 = self.factory.post('/fake-url')
        request_user1_likes_user2.user = self.user1
        serializer_user1_likes_user2 = LikeSerializer(data={'target_user_id': self.user2.pk}, context={'request': request_user1_likes_user2})
        if serializer_user1_likes_user2.is_valid():
            serializer_user1_likes_user2.save()
        
        # User2 likes User1, expecting a match
        request_user2_likes_user1 = self.factory.post('/another-fake-url')
        request_user2_likes_user1.user = self.user2
        serializer_user2_likes_user1 = LikeSerializer(data={'target_user_id': self.user1.pk}, context={'request': request_user2_likes_user1})
        
        if serializer_user2_likes_user1.is_valid():
            serializer_user2_likes_user1.save()

            match_exists = Like.objects.filter(source_user=self.user2, target_user=self.user1).exists() and Like.objects.filter(source_user=self.user1, target_user=self.user2).exists()

            self.assertTrue(match_exists)

            self.assertEqual(Like.objects.count(), 2)