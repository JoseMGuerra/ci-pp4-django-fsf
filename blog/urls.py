
from django.urls import path
from . import post_views
from . import comment_views
from . import backend_views
from . import category_views

app_name = "blog"

urlpatterns = [
    path('create/', post_views.post_create, name='post-create'),
    path('posts/', post_views.post_list, name='post-list'),
    path('post/<slug>/', post_views.post_detail, name='post-detail'),
    path('post/<slug>/update/', post_views.post_update, name='post-update'),
    path('post/<slug>/delete/', post_views.post_delete, name='post-delete'),
    path('likes/<slug>', post_views.post_like, name='post-like'),

    path('post/<slug>/comment/', comment_views.post_comment, name='post-comment'),
    
    path('posts/management/backend/', backend_views.posts_management, name='posts-management'),
    path('posts/<slug>/post_backend_delete/backend/', backend_views.post_backend_delete, name='post-backend-delete'),

    path('category/<category_slug>/', category_views.posts_by_category, name='posts-by-category'),
]
