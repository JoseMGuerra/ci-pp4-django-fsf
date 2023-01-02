from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from blog.models import Post
from blog.forms import PostForm


@login_required
def profile(request):
    """
    Handle requests to the /profile/ URL, and render the profile template.

    Displays the user's profile, as well as a paginated list of posts.

    Parameters:
        request (HttpRequest): The incoming request.

    Returns:
        HttpResponse: The rendered template, containing the profile and posts.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    my_posts = Post.objects.filter(author=request.user)

    paginator = Paginator(my_posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    template = "profiles/profile.html"
    context = {
        "page_title": "Profile",
        "profile": profile,
        "posts": posts,
        "page": page,
    }
    return render(request, template, context)


@login_required
def profile_settings(request):
    """
    Allow a user to update their profile settings,
    including their profile image.

    Parameters:
        request (HttpRequest): The incoming request.

    Returns:
        HttpResponse: The rendered response.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(request.POST, request.FILES, instance=profile)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your profile has been successfully updated.")
            return redirect(reverse("profile"))
        else:
            form = UserProfileForm(instance=profile)

    template = "profiles/profile_settings.html"
    context = {
        "page_title": "Profile Image",
        "profile": profile,
        "form": form,
    }
    return render(request, template, context)
