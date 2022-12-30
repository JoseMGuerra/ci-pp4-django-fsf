from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from blog.models import Post, Comment, Category
from blog_settings.urls import handler403
User = get_user_model()


class TestViews(TestCase):
    """Test blog_setting views"""

    @classmethod
    def setUpTestData(cls):
        """Create test data"""

        cls.superuser = User.objects.create_superuser(username='admin')
        cls.superuser.set_password('password')
        cls.superuser.save()

        cls.user = User.objects.create(username='testuser')
        cls.user.set_password('abc123')
        cls.user.save()

    def setUp(self):
        self.category = Category.objects.create(
            name="Django",
            slug="django",
        )
        self.post = Post.objects.create(
                category=self.category,
                title='test title',
                slug='test-title',
                author=self.user,
                content='test content',
                approved='True',
                featured='True',
                status='published',
        )

        self.comment = Comment.objects.create(
            post=self.post,
            user=self.user,
            body='test comment',
            approved='True'
        )

    # def test_error_handler403_GET(self):
    #     """Test error handler 403 retrieval and template used"""
    #     response = self.client.get('')
    #     self.assertEqual(response.status_code, 403)
    #     self.assertTemplateUsed(response, 'errors/errors_base.html')
    #     self.assertTemplateUsed(response, 'errors/403.html')
