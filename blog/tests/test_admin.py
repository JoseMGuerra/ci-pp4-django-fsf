from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from blog.models import Post, Comment, Category
User = get_user_model()


class TestPostAdmin(TestCase):
    """
    Test Post Admin
    """
    @classmethod
    def setUpTestData(cls):
        """Create test data"""

        # create a superuser
        cls.superuser = User.objects.create_superuser(
            username='admin',
            email='admin@email.com',
            password='password'
            )
        cls.superuser.save()

        # create a user
        cls.user = User.objects.create(
            username='testuser',
            password='abc123')
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
                approved='False',
                featured='False',
                status='published',
        )

        # create a comment for testing
        self.comment = Comment.objects.create(
            post=self.post,
            user=self.user,
            body='test comment',
            approved='False'
        )

    def test_post_is_featured(self):
        """Test post is featured"""

        # Log in as superuser / staff
        login = self.client.login(username='admin', password='password')

        # count how many posts are currently featured
        featured = Post.objects.filter(featured=True).count()
        self.assertTrue(self.post.featured)

        data = {
            'action': 'featured',
            '_selected_action': [self.post.id, ]
            }

        response = self.client.post(
            reverse('admin:blog_post_changelist'), data, follow=True)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # count how many posts are currently featured
        self.assertEqual(
            Post.objects.filter(featured=True).count(), featured+1)

    def test_post_is_approved(self):
        """Test post is approved"""

        # Log in as superuser / staff
        login = self.client.login(username='admin', password='password')

        # count how many posts are currently approved
        approved = Post.objects.filter(approved=True).count()
        self.assertTrue(self.post.approved)

        data = {
            'action': 'approved',
            '_selected_action': [self.post.id, ]
            }

        response = self.client.post(
            reverse('admin:blog_post_changelist'), data, follow=True)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # check number of approved posts has increased by one
        self.assertEqual(
            Post.objects.filter(approved=True).count(), approved+1)

    def test_approved_comments(self):
        """Test comment is approved"""

        # Log in as superuser / staff
        login = self.client.login(username='admin', password='password')

        # count how many comments are currently approved
        approved = Comment.objects.filter(approved=True).count()
        self.assertTrue(self.comment.approved)

        data = {
            'action': 'approved',
            '_selected_action': [self.comment.id, ]
            }

        response = self.client.post(
            reverse('admin:blog_comment_changelist'), data, follow=True)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # check number of approved comments has increased by one
        self.assertEqual(
            Comment.objects.filter(approved=True).count(), approved+1)
