from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Form for posts
    """
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'category',
            'featured_image',
            'status',
            ]


class AdminPostForm(PostForm):
    """
    AdminForm for posts
    """
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'category',
            'featured_image',
            'approved',
            'featured',
            'status',
        ]


class CommentForm(forms.ModelForm):
    """
    Form for comment
    """
    class Meta:
        model = Comment
        fields = ['body']
