from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    )
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger
from .models import Post, Comment, Category
from .forms import AdminPostForm, PostForm, CommentForm
from django.contrib import messages
from django.http import JsonResponse


def post_list(request):
    """
    Display all posts
    """
    post_list = Post.objects.filter(status="published", approved=True)
    paginator = Paginator(post_list, 3)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    template = ["blog/post/post_list.html"]
    context = {
        "page_title": "Posts",
        "posts": posts,
        "page": page,
    }
    return render(request, template, context)


def post_detail(request, slug):
    """
    Display a single post and a comment form
    """
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True)
    form = CommentForm()

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    template = "blog/post/post_detail.html"
    context = {
        "page_title": "Post",
        "comments": comments,
        "form": form,
        "post": post,
        "liked": liked,
    }
    return render(request, template, context)


@login_required
def post_create(request):
    """
    Create a new post
    """
    if request.user.is_staff:
        form = AdminPostForm(
            request.POST or None,
            request.FILES or None)
    else:
        form = PostForm(
            request.POST or None,
            request.FILES or None)

    author = request.user

    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            post = form.save(commit=False)
            post.save()
            messages.success(
                request, "Your post is being reviewed.")

            return redirect(reverse("blog:post-detail", kwargs={
                "slug": form.instance.slug
            }))
        else:
            form = PostForm()

    template = "blog/post/post_create.html"
    context = {
        "page_title": "Add",
        "form_type": "Add",
        "form": form,
    }
    return render(request, template, context)


@login_required
def post_update(request, slug):
    """
    Update the post
    """
    post = get_object_or_404(Post, slug=slug)

    if request.user.is_staff:
        form = AdminPostForm(
            request.POST or None,
            request.FILES or None,
            instance=post)
    else:
        form = PostForm(
            request.POST or None,
            request.FILES or None,
            instance=post)

    if (request.user != post.author) and not request.user.is_staff:
        return redirect(reverse("homepage"))

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your post has been successfully updated.")
            return redirect(reverse("blog:post-detail", kwargs={
                "slug": form.instance.slug
            }))
        else:
            form = PostForm(instance=post)

    template = "blog/post/post_create.html"
    context = {
        "page_title": "Update",
        "form_type": "Update",
        "form": form,
    }
    return render(request, template, context)


@login_required
def post_delete(request, slug):
    """
    Delete a post
    """
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        post.delete()
        messages.success(
            request, "You post has been deleted.")
        return redirect(reverse("blog:post-list"))
    else:
        form = PostForm(instance=post)

    template = "blog/includes/delete_modal.html"
    context = {
        "form_type": "Delete",
        "post": post,
        "form": form,
    }
    return render(request, template, context)


@login_required
def post_like(request, slug, *args, **kwargs):
    """
    LKes a post
    """
    post = get_object_or_404(Post, slug=slug)
    liked = False
    if request.method == "POST":
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True
            messages.success(
                request, "Liked!")
        data = {
            "liked": liked,
            "likes_count": post.likes.count(),
        }
        return JsonResponse(data, safe=False)
