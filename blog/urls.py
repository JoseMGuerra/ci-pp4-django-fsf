
from django.urls import path
from . import views
from . import comment_views
from . import backend_views
from . import category_views

app_name = "blog"

urlpatterns = [
    path('create/', views.post_create, name='post-create'),
    path('posts/', views.post_list, name='post-list'),
    path('post/<slug>/', views.post_detail, name='post-detail'),
    path('post/update/<slug>/', views.post_update, name='post-update'),
    path('post/delete/<slug>/', views.post_delete, name='post-delete'),
    path('post/likes/<slug>', views.post_like, name='post-like'),
    path(
        'post/comment/<slug>/',
        comment_views.post_comment, name='post-comment'),
    path(
        'posts/backend/management/',
        backend_views.posts_management, name='posts-management'),
    path(
        'posts/<slug>/backend/post_backend_delete/',
        backend_views.post_backend_delete, name='post-backend-delete'),
    path(
        'post/category/<category_slug>/',
        category_views.posts_by_category, name='posts-by-category'),
]
