from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from profiles.models import UserProfile
User = get_user_model()
UserProfile = User


class TestUserProfileModel(TestCase):
    """
    Test UserProfile model
    """
    def setUp(self):
        self.user = UserProfile.objects.create(
            username='testuser',
            email='testuser@email.com',
            )
        self.user.set_password('abc123')
        self.user.save()

    def test_user_profile_model_name_str_(self):
        """Test UserProfile model return name"""
        data = self.user
        self.assertEqual(
            data.__str__(), 'testuser')
