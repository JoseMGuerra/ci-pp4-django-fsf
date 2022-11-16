from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    )
from django.utils.text import slugify
from .models import Post
from .forms import PostForm


def post_list(request):
    """
    Display all posts
    """
    post_list = Post.objects.all()

    template = ["blog/post_detail.html"]
    context = {
        "page_title": "Posts",
        "post_list": post_list,
    }
    return render(request, template, context)
    pass


def post_detail(request):
    pass


def post_create(request):
    """
    Create a new post
    """
    form = PostForm(request.POST or None, request.FILES or None)
    author = request.user
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            post = form.save(commit=False)
            post.save()
            return redirect(reverse("post-list", kwargs={
                "slug": form.instance.slug
            }))
        else:
            form = PostForm()

    template = "blog/post_create.html"
    context = {
        "page_title": "Create",
        "form_type": "Create",
        "form": form,
    }
    return render(request, template, context)


def post_update(request):
    pass


def post_delete(request):
    pass
