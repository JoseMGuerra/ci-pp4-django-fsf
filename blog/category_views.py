from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    )
from .models import Post, Category


def posts_by_category(request, category_slug):
    categories = Category.objects.all()
    posts = Post.objects.filter(status="published", approved=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)

    template = "blog/category/posts_by_category.html"
    context = {
        "categories": categories,
        "posts": posts,
        "category": category,
    }
    return render(request, template, context)
