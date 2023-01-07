from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
    reverse,
    )
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger
from .models import Post, Comment, Category
from .forms import AdminPostForm, PostForm, CommentForm
from django.contrib import messages
from django.http import JsonResponse


def post_list(request):
    """
    Display a list of published and approved posts, paginated.

    Parameters:
        request (HttpRequest): the HTTP request object

    Returns:
        HttpResponse: the HTTP response object with the rendered template
    """
    post_list = Post.objects.filter(status="published", approved=True)
    categories = Category.objects.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    template = ["blog/post/post_list.html"]
    context = {
        "page_title": "Coding Articles",
        "posts": posts,
        "categories": categories,
        "page": page,
    }
    return render(request, template, context)


def post_detail(request, slug):
    """
    Display a single post and a comment form.

    Parameters:
        request (HttpRequest): The HTTP request made to the view.
        slug (str): The slug identifier for the post.

    Returns:
        HttpResponse: The rendered HTML template for the post detail page.
    """
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True)
    form = CommentForm()

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    template = "blog/post/post_detail.html"
    context = {
        "page_title": "Coding Article Detail",
        "comments": comments,
        "form": form,
        "post": post,
        "liked": liked,
    }
    return render(request, template, context)


@login_required
def post_create(request):
    """
    Create a new post.

    If the request method is POST, and the form data is valid,
    a new post will be created with the provided data. The form
    used depends on whether the
    user making the request is an administrator.
    If the user is a staff member, the post will be visible to staff
    users only.
    If the user is not a staff member,
    the post will be visible to all users.

    If the request method is GET, or the form data is invalid,
    the form will be rendered for the user to fill out and submit.

    Args:
        request: An HTTP request object.

    Returns:
        An HTTP response object with the appropriate status code and content.
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
        "page_title": "Add Post",
        "form_type": "Add",
        "form": form,
    }
    return render(request, template, context)


@login_required
def post_update(request, slug):
    """
    Update an existing blog post.

    This view handles POST requests to update a blog post with a given slug. It
    first retrieves the post to be updated from the database and then renders a
    form for the user to edit the post. The form used depends on whether the
    user making the request is an administrator. If the request method is POST,
    the form is validated and, if valid, the post is updated and a success
    message is displayed to the user. If the form is invalid or the request
    method is not POST, the form is re-rendered with the existing post data.

    Parameters:
        request: an HTTP POST request to update the post.
        slug: a string representing the unique slug for the post.

    Returns:
        An HTTP response containing the rendered form for updating the post or
        a redirect to the updated post detail page.
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
        return redirect(reverse("home:homepage"))

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
        "page_title": "Update Post",
        "form_type": "Update",
        "form": form,
    }
    return render(request, template, context)


@login_required
def post_delete(request, slug):
    """
    Delete a post with the given slug.

    Accepts a POST request with a slug parameter and deletes the post
    with the given slug from the database.
    On GET request, render a confirmation form.

    Parameters:
        request: the request object
        slug: the slug of the post to delete

    Returns:
        On a POST request:
            A redirect to the post list page
        On a GET request:
            A rendered form template to confirm the post deletion
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
    Handles a POST request to like a blog post.

    Parameters:
        request (HttpRequest): The request object containing the POST data.
        slug (str): The slug of the post to be liked.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        JsonResponse: A JSON response containing the new value of
        'liked' (True if the post was liked, False otherwise)
        and the new number of likes. If the request method is not a
        POST request, returns an HTTP 405 (Method Not Allowed) response.

    Raises:
        Http404: If no post with the specified slug exists.
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


def search(request):
    """
    Search for a post based on a search query.

    Parameters:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object with the search results.
    """
    query = request.GET.get("query", "")

    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(category__name__icontains=query) |
            Q(author__username__icontains=query)
        )
    else:
        posts = []

    template = "blog/post/search.html"
    context = {
        "page_title": "Search Coding Article",
        "query": query,
        "posts": posts,
        }

    return render(request, template, context)
