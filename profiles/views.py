from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import UserProfile
from .forms import UserProfileForm
from blog.models import Post
from blog.forms import PostForm


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    my_posts = Post.objects.filter(author=request.user)
    paginator = Paginator(my_posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    template = "profiles/profile.html"
    context = {
        "profile": profile,
        "page_title": "Profile",
        "posts": posts,
        "page": page,
    }
    return render(request, template, context)
