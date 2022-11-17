
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.post_create, name='post-create'),
    path('posts/', views.post_list, name='post-list'),
    path('post/<slug>/', views.post_detail, name='post-detail'),
    path('post/<slug>/update/', views.post_update, name='post-update'),
    path('post/<slug>/delete/', views.post_delete, name='post-delete'),
    path('likes/<slug>', views.post_like, name='post-like'),
]
