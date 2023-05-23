from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
	search_fields = ['content']
admin.site.register(Post, PostAdmin)