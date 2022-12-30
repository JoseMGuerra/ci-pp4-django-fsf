from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from blog.models import Post, Comment, Category
User = get_user_model()


class TestCategoryModel(TestCase):
    """
    Test category model
    """
    def setUp(self):
        self.cat1 = Category.objects.create(name='Django', slug='django')

    def test_category_model_entry(self):
        """Test Category model field attributes"""
        data = self.cat1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name_str_(self):
        """Test Category model return name"""
        data = self.cat1
        self.assertEqual(
            data.__str__(), 'Django')

    def test_category_absolute_url(self):
        """ Test the get_absolute_url method for category"""
        data = self.cat1
        self.assertEqual(
            data.get_absolute_url(), '/blog/post/category/django/')


class TestPostModel(TestCase):
    """
    Test Post model
    """
    def setUp(self):
        Category.objects.create(name='Django', slug='django'),
        User.objects.create(username='admin',),
        self.post1 = Post.objects.create(
            category_id=1,
            title='test title',
            slug='test-title',
            author_id=1,
            content='test content',
        )

    def test_post_model_entry(self):
        """Test Post model field attributes"""
        data = self.post1
        self.assertTrue(isinstance(data, Post))

    def test_post_model_str_(self):
        """Test Post model return name"""
        data = self.post1
        self.assertEqual(
            data.__str__(), 'Post: test title by admin')

    def test_post_absolute_url(self):
        """Test the get_absolute_url method for post"""
        data = self.post1
        self.assertEqual(
            data.get_absolute_url(), '/blog/post/test-title/')


class TestCommentModel(TestCase):
    """
    Test Comment model
    """
    def setUp(self):
        Category.objects.create(name='Django', slug='django'),
        User.objects.create(username='admin',),
        self.post1 = Post.objects.create(
            category_id=1,
            title='Test Title',
            slug='test-title',
            author_id=1,
            content='test content',
        )
        self.com1 = Comment.objects.create(
            post=self.post1,
            user_id=1,
            email='admin@email.com',
            body='test comment',
        )

    def test_comment_model_str_(self):
        """Test Comment model return name"""
        data = self.com1
        self.assertEqual(
            data.__str__(), 'admin')
