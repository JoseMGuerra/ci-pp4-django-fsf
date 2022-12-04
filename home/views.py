from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from blog.models import Post
from .forms import ContactForm
from django.template.loader import render_to_string


def home_view(request):
    """
    Home view function
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


@login_required
def contact(request):
    """
    Contact form
    """
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd.get('name')
            email = cd.get('email')
            content = cd.get('content')
            recipient = cd.get('email')

            subject = 'Blog Enquiry'
            message = 'Sending Email through Gmail'
            html = render_to_string("home/emails/contact_form.html", {
                "name": name,
                "email": email,
                "content": content,
            })
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [recipient],
                fail_silently=False,
                html_message=html
                )

            messages.success(request, 'Email Sent!!')
            return redirect('home:homepage')
    else:
        ContactForm()

    template = 'home/contact.html'
    context = {
        'form': form
    }
    return render(request, template, context)
