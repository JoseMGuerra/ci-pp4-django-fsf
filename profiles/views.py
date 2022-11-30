from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
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
        "page_title": "Profile",
        "profile": profile,
        "posts": posts,
        "page": page,
    }
    return render(request, template, context)


def change_image(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(request.POST, request.FILES, instance=profile)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your profile image has been successfully updated.")
            return redirect(reverse("profile"))
        else:
            form = UserProfileForm(instance=profile)

    template = "profiles/change_image.html"
    context = {
        "page_title": "Profile Image",
        "profile": profile,
        "form": form,
    }
    return render(request, template, context)
