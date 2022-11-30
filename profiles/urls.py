from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('change_image/', views.change_image, name='change-image'),
]
