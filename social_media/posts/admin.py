from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)


admin.site.register(Post, PostAdmin)
