from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from blog.models import Post
from blog.forms import PostForm


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    my_posts = Post.objects.filter(author=request.user)

    template = "profiles/profile.html"
    context = {
        "profile": profile,
        "page_title": "Profile",
        "my_posts": my_posts,
    }
    return render(request, template, context)
