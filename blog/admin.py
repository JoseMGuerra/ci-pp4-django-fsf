from django.contrib import admin
from .models import Post
from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Post model in admin panel
    """
    list_display = (
        'title', 'slug', 'status', 'created_on',
        'updated_on', 'approved', 'featured')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    actions = ['select_as_featured', 'deselect_as_featured']

    def select_as_featured(self, request, queryset):
        queryset.update(featured=True)

    def deselect_as_featured(self, request, queryset):
        queryset.update(featured=False)
