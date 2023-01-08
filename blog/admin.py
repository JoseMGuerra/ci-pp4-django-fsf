from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
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
class PostAdmin(SummernoteModelAdmin):
    """
    Post model in admin panel
    """
    summernote_fields = ('content',)

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
class CommentAdmin(SummernoteModelAdmin):
    """
    Comment model in admin panel
    """
    summernote_fields = ('body',)

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
