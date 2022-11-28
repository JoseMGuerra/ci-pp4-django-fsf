from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Post(models.Model):
    """
    Database model for Posts
    """
    class Status(models.TextChoices):
        DRAFT = "Draft", "Draft"
        PUBLISHED = "Published", "Published"

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.DRAFT)
    featured_image = models.ImageField(
        upload_to="media/images/", blank=True, null=True, default="placeholder")
    approved = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        User, related_name='blogpost_likes', blank=True)

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
    approved = models.BooleanField(default=True)

    class Meta:
        """Sets the order of comments by date ascending"""
        ordering = ["created_on"]

    def __str__(self):
        """Returns comment with body and name"""
        return self.user.username
