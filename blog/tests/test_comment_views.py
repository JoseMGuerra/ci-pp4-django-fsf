from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from blog.models import Post, Comment, Category
User = get_user_model()


class TestViews(TestCase):
    """
    Test blog app views
    """
    @classmethod
    def setUpTestData(cls):
        """Create test data"""

        # create a superuser
        cls.superuser = User.objects.create_superuser(username='admin')
        cls.superuser.set_password('password')
        cls.superuser.save()

        # create a user
        cls.user = User.objects.create(username='testuser')
        cls.user.set_password('abc123')
        cls.user.save()

    def setUp(self):
        # create a category for testing
        self.category = Category.objects.create(
            name="Django",
            slug="django",
        )

        # create a post for testing
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

        # create a comment for testing
        self.comment = Comment.objects.create(
            post=self.post,
            user=self.user,
            body='test comment',
            approved='True',
        )

    def test_post_comment_POST(self):
        """Test post comment created and template used"""

        # Log in the user
        login = self.client.login(username='admin', password='password')
        login = self.client.login(user='testuser', password='abc123')

        # Access the post-comment view
        response = self.client.post(
            reverse('blog:post-comment',
                    args=[self.post.slug]),
            data={'body': 'test comment'})

        # Check redirect to correct template
        self.assertRedirects(
            response, reverse('blog:post-detail', args=[self.post.slug]))

    def test_post_comment_GET(self):
        """Test comment retrieval and template used"""

        # Log in the user
        login = self.client.login(username='admin', password='password')
        login = self.client.login(user='testuser', password='abc123')

        # Access the post-comment view
        response = self.client.get(
            reverse('blog:post-comment', args=[self.post.slug]))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that is the correct template used
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'blog/post/post_detail.html')
