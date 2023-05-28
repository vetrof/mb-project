from django.contrib import admin

from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('text',)
    ordering = ('id',)
    search_fields = ('text',)


admin.site.register(Post, PostAdmin)
