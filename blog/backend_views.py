from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    )
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def posts_management(request):
    """
    Display all posts
    """
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    template = ["blog/backend/posts_management.html"]
    context = {
        "page_title": "Posts Management",
        "posts": posts,
        "page": page,
    }
    return render(request, template, context)


def post_backend_delete(request, slug):
    """
    Delete a post in the backend
    """
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        post.delete()
        messages.success(
            request, "You post has been deleted.")
        if not request.user.is_staff:
            return redirect('profile')
        else:
            return redirect("blog:posts-management")
    else:
        form = PostForm(instance=post)

    template = "blog/backend/post_backend_delete.html"
    context = {
        "form_type": "Delete",
        "post": post,
        "form": form,
    }
    return render(request, template, context)
