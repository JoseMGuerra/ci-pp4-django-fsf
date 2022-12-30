from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, PageNotAnInteger
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
            approved='True'
        )

    def test_posts_management_GET(self):
        """Test management posts retrieval and template used"""

        # Log in as superuser / staff
        login = self.client.login(username='admin', password='password')

        # Access the post-management view
        response = self.client.get('/blog/posts/backend/management/')

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that is the correct template used
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'blog/backend/posts_management.html')

    def test_post_backend_delete_GET(self):
        """Test post backend delete retrieval and template used"""

        # Log in as superuser / staff
        login = self.client.login(username='admin', password='password')

        # Access the post-backend delete view
        response = self.client.get(
            reverse('blog:post-backend-delete', args=[self.post.slug]))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that is the correct template used
        self.assertTemplateUsed(
            response, 'blog/backend/post_backend_delete.html')

    def test_staff_post_backend_delete_POST(self):
        """Test staff post backend delete and template used"""

        # Log in as superuser / staff
        login = self.client.login(username='admin', password='password')

        # Access the post-backend delete view
        response = self.client.post(
            reverse('blog:post-backend-delete',
                    args=[self.post.slug]),
            data={'post': self.post})

        # Check redirect to correct template
        self.assertRedirects(
            response, reverse('blog:posts-management'))

    def test_user_post_backend_delete_POST(self):
        """Test user post backend delete and template used"""

        # Log in as user
        login = self.client.login(username='testuser', password='abc123')

        # Access the post-backend delete view
        response = self.client.post(
            reverse('blog:post-backend-delete',
                    args=[self.post.slug]),
            data={'post': self.post})

        # Check redirect to correct template
        self.assertRedirects(
            response, reverse('profile'))
