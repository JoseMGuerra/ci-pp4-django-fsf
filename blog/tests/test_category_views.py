from django.test import TestCase
from django.urls import reverse
from blog.models import Category


class TestViews(TestCase):
    """
    Test blog app views
    """
    def setUp(self):
        """Create test data"""

        # create a category for testing
        self.category = Category.objects.create(
            name="Django",
            slug="django",
        )

    def test_posts_by_category_GET(self):
        """Test category retrieval and template used"""

        # Access the post-by_category view
        response = self.client.get(
            reverse('blog:posts-by-category', args=[self.category.slug]))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that is the correct template used
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(
            response, 'blog/category/posts_by_category.html')
