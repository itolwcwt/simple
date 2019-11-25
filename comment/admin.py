from django.contrib import admin
from . models import Comment

admin.site.site_title = '评论'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'user', 'body'[:10], 'created',)
    ordering = ('-id',)
    list_per_page = 20
