from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    )
from django.views.decorators.http import require_POST
from django.utils.text import slugify
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def posts_by_category(request, category_slug):
    categories = Category.objects.all()
    posts = Post.objects.filter(status="published", approved=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)

    template = "blog/posts_by_category.html"
    context = {
        "categories": categories,
        "posts": posts,
        "category": category,
    }
    return render(request, template, context)


def post_list(request):
    """
    Display all posts
    """
    post_list = Post.objects.filter(status="published", approved=True)
    most_recent = Post.objects.order_by("-created_on")[:3]

    template = ["blog/post_list.html"]
    context = {
        "page_title": "Posts",
        "post_list": post_list,
        "most_recent": most_recent,
    }
    return render(request, template, context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True)
    form = CommentForm()

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    template = "blog/post_detail.html"
    context = {
        "page_title": "Post",
        "comments": comments,
        "form": form,
        "post": post,
        "liked": liked,
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
            messages.success(
                request, "Your post is being reviewed.")

            return redirect(reverse("blog:post-detail", kwargs={
                "slug": form.instance.slug
            }))
        else:
            form = PostForm()

    template = "blog/post_create.html"
    context = {
        "page_title": "Add",
        "form_type": "Add",
        "form": form,
    }
    return render(request, template, context)


def post_update(request, slug):
    """
    Update the post
    """
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
            messages.success(
                request, "Your post has been successfully updated.")
            return redirect(reverse("blog:post-detail", kwargs={
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


def post_like(request, slug, *args, **kwargs):
    """
    LKes a post
    """
    post = get_object_or_404(Post, slug=slug)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)

    else:
        post.likes.add(request.user)
        messages.success(
            request, "Thank you for liking the post.")

    return HttpResponseRedirect(reverse("blog:post-detail", args=[slug]))


@require_POST
def post_comment(request, slug):
    """
    Create a new comment
    """
    post = get_object_or_404(
        Post, slug=slug, status="published", approved=True)
    comment = None

    form = CommentForm(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.email = request.user.email
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(reverse("blog:post-detail", kwargs={
                "slug": post.slug
            }))

    else:
        form = CommentForm()

    template = 'blog/post_detail.html'
    context = {
        "post": post,
        "comment": comment,
        "form": form,
    }
    return render(request, template, context)


def posts_management(request):
    """
    Display all posts
    """
    post_list = Post.objects.all()
    most_recent = Post.objects.order_by("-created_on")

    template = ["blog/posts_management.html"]
    context = {
        "page_title": "Posts Management",
        "post_list": post_list,
        "most_recent": most_recent,
    }
    return render(request, template, context)
