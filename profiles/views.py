from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    profile = get_object_or_404(UserProfile)

    template = "profiles/profile.html"
    context = {
        "profile": profile,
        "page_title": "Profile"
    }
    return render(request, template, context)
