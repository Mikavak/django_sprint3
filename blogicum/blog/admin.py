from django.contrib import admin

from .models import Category, Post, Location


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'author')
    list_editable = ('is_published',)
    list_filter = ('category',)
    search_fields = ('title', )


class CategotyAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategotyAdmin)
admin.site.register(Location)
