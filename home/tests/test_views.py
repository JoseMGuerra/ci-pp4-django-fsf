from django.core import mail
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from blog.models import Post, Category, Comment
from home.forms import ContactForm
User = get_user_model()


class HomeViewTestCase(TestCase):
    """
    Test Home app views
    """
    def setUp(self):
        """Create test data"""

        # Create a user for testing the contact form
        User.objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='abc123',
        )

    def test_home_view(self):
        # Access the home view as an anonymous user
        response = self.client.get(reverse('home:homepage'))

        # Test that the response is successful
        self.assertEqual(response.status_code, 200)

        # Test that the correct template is used
        self.assertTemplateUsed(response, 'home/index.html')

        # Test that the featured posts and most recent posts are in the context
        self.assertIn('featured_post_list', response.context)
        self.assertIn('most_recent', response.context)

    def test_about_view(self):
        """Test the about page view"""
        # Send a GET request to the about page
        response = self.client.get(reverse('home:about'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains the correct page title
        self.assertEqual(response.context['page_title'], "About")

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'home/about.html')

    def test_contact_view(self):
        # Log in as the test user
        self.client.login(username='testuser', password='abc123')

        # Send a POST request to the contact form with valid form data
        response = self.client.post(reverse('home:contact'), {
            'name': 'Test User',
            'email': 'testuser@email.com',
            'recipient': 'admin@example.com',
            'content': 'Test message',
        })

        # Check that the response is a redirect to the homepage
        self.assertRedirects(response, reverse('home:homepage'))

    def test_contact_view_invalid_form(self):
        # Log in as the test user
        self.client.login(username='testuser', password='abc123')

        # Send a POST request to the contact form with invalid form data
        response = self.client.post(reverse('home:contact'), {
            'name': '',
            'email': 'testuser@email.com',
            'recipient': '',
            'content': 'Test message'
        })
