
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('create/', views.post_create, name='post-create'),
    path('posts/', views.post_list, name='post-list'),
    path('post/<slug>/', views.post_detail, name='post-detail'),
    path('category/<category_slug>/', views.posts_by_category, name='posts-by-category'),
    path('post/<slug>/comment/', views.post_comment, name='post-comment'),
    path('post/<slug>/update/', views.post_update, name='post-update'),
    path('post/<slug>/delete/', views.post_delete, name='post-delete'),
    path('likes/<slug>', views.post_like, name='post-like'),
    path('posts/management/', views.posts_management, name='posts-management'),
    path('posts/<slug>/post_backend_delete/', views.post_backend_delete, name='post-backend-delete'),
]
