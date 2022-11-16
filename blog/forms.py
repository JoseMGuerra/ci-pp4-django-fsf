from django.forms import ModelForm
from cloudinary.forms import CloudinaryFileField

from .models import Post


class PostForm(ModelForm):
    """
    Form for comments
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image']
