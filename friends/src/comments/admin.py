from django.contrib import admin
from .models import Comment
class CommentAdmin(admin.ModelAdmin):
	search_fields = ['content']
admin.site.register(Comment, CommentAdmin)