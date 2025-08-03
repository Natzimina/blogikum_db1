
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published')
    search_fields = ('title',)
    list_filter = ('is_published', 'created_at')
    ordering = ('-created_at',)

