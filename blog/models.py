from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Category(models.Model):
    """
    Database model for Category
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200, unique=True)

    class Meta:
        """
        Set the order of categories by ascending order
        Set the plural name for category
        """
        ordering = ["name"]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        """Returns category name"""
        return self.name

    def get_absolute_url(self):
        """ Get the post category absolute url """
        return reverse("blog:posts-by-category", args=[self.slug])


class Post(models.Model):
    """
    Database model for Posts
    """
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.DRAFT)
    featured_image = models.ImageField(
        upload_to="media/images/", default="placeholder")
    approved = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        User, related_name='blogpost_likes', blank=True)
    like_count = models.BigIntegerField(default="0")

    class Meta:
        """Set the order of posts by descending date """
        ordering = ["-created_on"]

    def __str__(self):
        """Returns a string representation of the object"""
        return f"Post: {self.title} by {self.author}"

    def save(self, *args, **kwargs):
        """Save method override with slugify"""
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """ Get the post detail absolute url """
        return reverse("blog:post-detail", args=[self.slug])

    def number_of_likes(self):
        """ Count number of likes """
        return self.likes.count()


class Comment(models.Model):
    """
    Database model for comments
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_comments")
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """Sets the order of comments by date ascending"""
        ordering = ["created_on"]

    def __str__(self):
        """Returns comment username"""
        return self.user.username
