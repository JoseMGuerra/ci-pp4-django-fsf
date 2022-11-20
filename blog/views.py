from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    )
from django.utils.text import slugify
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def post_list(request):
    """
    Display all posts
    """
    post_list = Post.objects.filter(status=1, approved=True)
    most_recent = Post.objects.order_by('-created_on')[:3]

    template = ["blog/post_list.html"]
    context = {
        "page_title": "Posts",
        "post_list": post_list,
        "most_recent": most_recent,
    }
    return render(request, template, context)
    pass


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True)
    new_comment = None

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    comment_form = CommentForm(data=request.POST)
    if request.method == 'POST':
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.success(request, "Your comment is being reviewed.")

            return redirect(reverse("post-detail", kwargs={
                "slug": post.slug
            }))
    else:
        comment_form = CommentForm()

    template = "blog/post_detail.html"
    context = {
        "page_title": "Post",
        "form_type": "Comment",
        "post": post,
        "liked": liked,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
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
            messages.success(
                request, "Your post has been updated successfully.")
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
    messages.success(
        request, "You post has been deleted.")

    return redirect("post-list")


def post_like(request, slug, *args, **kwargs):
    """ LKes a post """
    post = get_object_or_404(Post, slug=slug)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)

    else:
        post.likes.add(request.user)
        messages.success(
            request, 'Thank you for liking the post.')

    return HttpResponseRedirect(reverse("post-detail", args=[slug]))
