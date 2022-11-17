from django import forms
from .models import UserProfile

from cloudinary.forms import CloudinaryFileField


class UserProfileForm(forms.ModelForm):
    """
    Form for comments
    """
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'bio']
