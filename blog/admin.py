from django.contrib import admin
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)


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
    list_filter = ('status', 'created_on')
    actions = [
        'published',
        'draft',
        'featured',
        'unfeatured',
        'approved',
        'disapproved',
        ]

    def published(self, request, queryset):
        queryset.update(status=1)

    def draft(self, request, queryset):
        queryset.update(status=0)

    def featured(self, request, queryset):
        queryset.update(featured=True)

    def unfeatured(self, request, queryset):
        queryset.update(featured=False)

    def approved(self, request, queryset):
        queryset.update(approved=True)

    def disapproved(self, request, queryset):
        queryset.update(approved=False)


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

    actions = ['approved', 'disapproved']

    def approved(self, request, queryset):
        queryset.update(approved=True)

    def disapproved(self, request, queryset):
        queryset.update(approved=False)
