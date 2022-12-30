from django.contrib import admin
from .models import Post, Comment, Category
from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category model in admin panel
    """
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Post model in admin panel
    """
    list_display = (
        'title',
        'status',
        'created_on',
        'updated_on',
        'approved',
        'featured'
        )
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'category', 'featured')
    actions = [
        'featured',
        'approved',
        ]

    def featured(self, request, queryset):
        queryset.update(featured=True)

    def approved(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Comment model in admin panel
    """
    list_display = [
        'user',
        'email',
        'post',
        'created_on',
        'approved',
    ]
    list_filter = [
        'approved',
        'created_on',
    ]
    search_fields = [
        'user',
        'email',
        'body',
    ]

    actions = ['approved']

    def approved(self, request, queryset):
        queryset.update(approved=True)
