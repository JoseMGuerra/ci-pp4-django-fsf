from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    )
from django.utils.text import slugify
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect


def post_list(request):
    """
    Display all posts
    """
    post_list = Post.objects.filter(status=1, approved=True)

    template = ["blog/post_list.html"]
    context = {
        "page_title": "Posts",
        "post_list": post_list,
    }
    return render(request, template, context)
    pass


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True
    template = "blog/post_detail.html"
    context = {
        "page_title": "Post",
        "liked": liked,
        "post": post,
    }
    return render(request, template, context)


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
            return redirect(reverse("post-detail", kwargs={
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


def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(
        request.POST or None,
        request.FILES or None,
        instance=post
        )
    author = request.user
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post-detail", kwargs={
                "slug": form.instance.slug
            }))
        else:
            form = PostForm(instance=post)

    template = "blog/post_create.html"
    context = {
        "page_title": "Update",
        "form_type": "Update",
        "form": form,
    }
    return render(request, template, context)


def post_delete(request, slug):
    """ Delete a post """
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect("post-list")


def post_like(request, slug, *args, **kwargs):
    """ LKes a post """
    post = get_object_or_404(Post, slug=slug)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse("post-detail", args=[slug]))
