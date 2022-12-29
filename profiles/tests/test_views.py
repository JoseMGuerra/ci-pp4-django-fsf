from django.test import TestCase
from django.urls import reverse
from blog.models import Post, Category
from django.contrib.auth import get_user_model
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
User = get_user_model()


class TestViews(TestCase):
    """
    Test profiles app views
    """
    @classmethod
    def setUp(self):
        """Create test data"""

        # create a superuser
        self.superuser = User.objects.create_superuser(username='admin')
        self.superuser.set_password('password')
        self.superuser.save()

        # create a user
        self.user = User.objects.create(
            username='testuser')
        self.user.set_password('abc123')
        self.user.save()

    def test_profile_GET(self):
        """Issue a GET request to the view and template used"""

        # Log in the user
        login = self.client.login(username='testuser', password='abc123')

        # Access the profile view as user
        response = self.client.get(reverse('profile'))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that is the correct template used
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_settings_GET(self):
        """Issue a GET request to the view and template used"""

        # Log in the user
        login = self.client.login(username='testuser', password='abc123')

        # Access the profile-settings view as user
        response = self.client.get(reverse('profile-settings'))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that is the correct template used
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'profiles/profile_settings.html')
