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
            approved='True'
        )

        # data for post create success
        self.form_data = {
            'title': 'Test Post',
            'content': 'This is a test post.',
            'status': 'published',
        }

    def test_post_list_view_GET(self):
        """Issue a GET request to the view and template used"""

        # Access the post-list view
        response = self.client.get(reverse('blog:post-list'))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that is the correct template used
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'blog/post/post_list.html')

    def test_post_detail_view_GET(self):
        """Issue a GET request to the view and template used"""

        # Access the post-detail view
        response = self.client.get(
            reverse('blog:post-detail', kwargs={'slug': self.post.slug}))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that is the correct template used
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'blog/post/post_detail.html')

    def test_user_post_create_GET(self):
        """Issue a GET request to the view and template used"""

        # Log in the user
        login = self.client.login(username='testuser', password='abc123')

        # Access the post-create view
        response = self.client.get(
            reverse('blog:post-create'))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that is the correct template used
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'blog/post/post_create.html')

    def test_staff_post_create_GET(self):
        """Issue a GET request to the view and template used"""

        # Log in the superuser
        login = self.client.login(username='admin', password='password')

        # Access the post-create view
        response = self.client.get(
            reverse('blog:post-create'))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that is the correct template used
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'blog/post/post_create.html')

    def test_post_create_success(self):
        """Issue a POST request to the view and template used"""

        # Log in the user
        login = self.client.login(username='admin', password='password')

        # Access the post-create view
        response = self.client.post(
            reverse('blog:post-create'), data=self.form_data)

        # Check that a post was created
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().title, 'test title')
        self.assertEqual(Post.objects.first().author, self.user)

    def test_user_post_update_GET(self):
        """Issue a GET request to the view and template used"""

        # Log in the user
        login = self.client.login(username='testuser', password='abc123')

        # Access the post-update view
        response = self.client.post(
            reverse('blog:post-update', args=[self.post.slug]))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that is the correct template used
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'blog/post/post_create.html')

    def test_staff_post_update_GET(self):
        """Issue a GET request to the view and template used"""

        # Log in as staff
        login = self.client.login(username='admin', password='password')

        # Access the post-update view
        response = self.client.get(
            reverse('blog:post-update', args=[self.post.slug]))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that is the correct template used
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'blog/post/post_create.html')

    def test_post_delete_GET(self):
        """Issue a GET request to the view and template used"""

        # Log in the user
        login = self.client.login(username='testuser', password='abc123')

        # Access the post-update view
        response = self.client.get(
            reverse('blog:post-delete', args=[self.post.slug]))

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that is the correct template used
        self.assertTemplateUsed(response, 'blog/includes/delete_modal.html')

    def test_user_post_delete_POST(self):
        """Issue a GET request to the view and template used"""

        # Log in the user
        login = self.client.login(username='testuser', password='abc123')

        # Access the post-update view
        response = self.client.post(
            reverse('blog:post-delete', args=[self.post.slug]),
            data={'post': self.post})

        # Check redirect to correct template
        self.assertRedirects(
            response, reverse('blog:post-list'))

    def test_post_like(self):
        """
        Issue a POST request to the view with AJAX request and template used
        """

        # Log in the user
        login = self.client.login(username='testuser', password='abc123')

        # Send a POST request to the view with an AJAX request
        response = self.client.post(
            reverse('blog:post-like', args=[self.post.slug]),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the user is added to the likes field of the post
        self.assertTrue(self.post.likes.filter(id=self.user.id).exists())

        # Check that the response contains the expected data
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'liked': True, 'likes_count': 1}
        )
        # Send another POST request to unlike the post
        response = self.client.post(
            reverse('blog:post-like', args=[self.post.slug]),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        # Check that the user is removed from the likes field of the post
        self.assertFalse(self.post.likes.filter(id=self.user.id).exists())

        # Check that the response contains the expected data
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'liked': False, 'likes_count': 0}
        )

    def test_search_view_with_query(self):
        """
        Issue a GET request to the search view with query
        """

        # Send a GET request to the view with a query in the GET parameters
        response = self.client.get(reverse("blog:search"), {"query": "test"})

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains the expected variables
        self.assertEqual(response.context["page_title"], "Search")
        self.assertEqual(response.context["query"], "test")
        # assuming 1 post matches the query
        self.assertEqual(len(response.context["posts"]), 1)

        # Check that the rendered HTML contains the expected content
        self.assertContains(response, "test")

    def test_search_view_without_query(self):
        """
        Issue a GET request to the search view without query
        """

        # Send a GET request to the view without a query in the GET parameters
        response = self.client.get(reverse("blog:search"))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains the expected variables
        self.assertEqual(response.context["page_title"], "Search")
        self.assertEqual(response.context["query"], "")
        self.assertEqual(len(response.context["posts"]), 0)

        # Check that the rendered HTML contains the expected content
        self.assertContains(response, "No posts matched your query...")
