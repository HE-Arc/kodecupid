from django.test import TestCase
from django.contrib.auth import get_user_model
from ..serializers import UserRegistrationSerializer
import logging

logger = logging.getLogger(__name__)

User = get_user_model()

class UserRegistrationSerializerTestCase(TestCase):
    def test_serializer_with_valid_data(self):
        """
        Test the serializer with valid data
        """
        valid_serializer_data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        serializer = UserRegistrationSerializer(data=valid_serializer_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')
        self.assertTrue(user.check_password(valid_serializer_data['password']))
        
    def test_serializer_with_invalid_data(self):
        """
        Test the serializer with invalid data (e.g., missing password)
        """
        invalid_serializer_data = {
            'username': 'testuser'
        }
        serializer = UserRegistrationSerializer(data=invalid_serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('password', serializer.errors)
        self.assertEqual(User.objects.count(), 0)

