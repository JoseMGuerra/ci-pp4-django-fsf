from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    )
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages


@login_required
def post_comment(request, slug):
    """
    Handle the creation and submission of a new comment.

    Parameters:
        request (HttpRequest): The incoming request object.
        slug (str): The unique slug identifier for the post.

    Returns:
        HttpResponse: The rendered template response.
    """
    post = get_object_or_404(Post, slug=slug, approved=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.email = request.user.email
            if request.user.is_staff:
                comment.approved = True
                comment.save()
                messages.success(request, "Thank you for your comment.")
            else:
                comment.save()
                messages.success(request, "Your comment it's been reviewed.")

            return redirect('blog:post-detail', slug=post.slug)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/post/post_detail.html', context)
