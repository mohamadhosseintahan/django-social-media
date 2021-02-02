from django.contrib import admin
from .models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    prepopulated_fields = {'slug': ('body',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'post', 'reply')
