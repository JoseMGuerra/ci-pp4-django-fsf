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


class AdminPostForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        """Remove body label and add placeholder text"""
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ''
        self.fields['body'].widget.attrs['placeholder'] = 'Add comment here...'
