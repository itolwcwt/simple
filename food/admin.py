from django.contrib import admin
from .models import Banner, Category, Article, Tui, Link, Tag

admin.site.site_title = '简单美食'
admin.site.site_header = '简单'


# 注册模型.
# 内容
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'img',  'category', 'tui', 'user', 'views', 'created_time', )
    list_per_page = 20
    ordering = ('-id',)
    list_display_links = ('id', 'title',)


# 图片
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')
    ordering = ('-id',)


# 分类
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'sort', 'title')
    ordering = ('id',)


# 推荐位
@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


# 接
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')


# 标签
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)
