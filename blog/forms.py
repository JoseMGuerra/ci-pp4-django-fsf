from django.forms import ModelForm
from cloudinary.forms import CloudinaryFileField

from .models import Post, Comment


class PostForm(ModelForm):
    """
    Form for comments
    """
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'featured_image',
            'status',
            ]


class CommentForm(ModelForm):
    """
    Form for posts
    """
    class Meta:
        model = Comment
        fields = ['body']
