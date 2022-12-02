from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    )
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages


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
            messages.success(
                request, "Thank you for your comment.")

            return redirect(reverse("blog:post-detail", kwargs={
                "slug": post.slug
            }))
    else:
        form = CommentForm()

    template = 'blog/post/post_detail.html'
    context = {
        "post": post,
        "comment": comment,
        "form": form,
    }
    return render(request, template, context)
