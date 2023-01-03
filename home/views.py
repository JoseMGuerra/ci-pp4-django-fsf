from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import render_to_string
from blog.models import Post
from .forms import ContactForm


def home_view(request):
    """
    Display the home page of the web app, featuring the three most
    recent and three most featured blog posts.

    Parameters:
        request (HttpRequest): The request made to the server.

    Returns:
        HttpResponse: The rendered home page template, with the most
        recent and featured blog posts in the context.
    """
    featured_post_list = Post.objects.filter(
        approved=True, featured=True, status="published"
        )[:3]
    most_recent = Post.objects.filter(
        approved=True, status="published"
        ).order_by("-created_on")[:3]

    template = ["home/index.html"]
    context = {
        "featured_post_list": featured_post_list,
        "most_recent": most_recent,
    }
    return render(request, template, context)


def about_view(request):
    """
    Render the about page template
    """
    template = ["home/about.html"]
    context = { 
        "page_title": "About",
    }

    return render(request, template, context)


@login_required
def contact(request):
    """
    Handle the contact form submission.

    Display a blank form when called with an HTTP GET request.
    When called with an HTTP POST request, validate the form data
    and send an email if the form is valid.

    Args:
        request: An HTTP request object.

    Returns:
        An HTTP response object containing the contact form.
    """
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd.get('name')
            email = request.user.email
            content = cd.get('content')
            recipient = cd.get('email')
            subject = 'My Coding Blog Enquiry'
            message = 'Email sent through Gmail'
            html = render_to_string("home/emails/contact_form.html", {
                "name": name,
                "email": email,
                "recipient": recipient,
                "content": content,
            })
            if name and email and content and recipient \
                    and subject and message and html:
                try:
                    send_mail(
                        subject,
                        message,
                        recipient,
                        [settings.EMAIL_HOST_USER],
                        fail_silently=False,
                        html_message=html
                        )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

                messages.success(request, 'Email Sent!!')
                return redirect('home:homepage')
    else:
        ContactForm()

    template = 'home/contact.html'
    context = {
        'form': form
    }
    return render(request, template, context)
