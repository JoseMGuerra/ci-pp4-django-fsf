from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("contact/", views.contact, name="contact"),
    path("about/", views.about_view, name="about"),
    path("", views.home_view, name="homepage"),

]
