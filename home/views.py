from django.shortcuts import render
from blog.models import Post


def home_view(request):
    featured_post_list = Post.objects.filter(
        approved=True, featured=True, status="published"
        )[:3]
    most_recent = Post.objects.filter(
        approved=True, status="published"
        ).order_by("-created_on")[:3]

    template = ["home/index.html"]
    context = {
        "featured_post_list": featured_post_list,
        "most_recent": most_recent,
    }
    return render(request, template, context)
