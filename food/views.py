from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_POST
from food.models import Banner, Category, Link, Article, Tag
from django.contrib.auth.decorators import login_required
from comment.models import Comment


# 全局
def repeat(request):
    alllinkurl = Link.objects.all()
    category = Category.objects.all()
    tags = Tag.objects.all()
    return locals()


# 首页
def index(request):
    banner = Banner.objects.filter(is_active=True)[0:4]
    allarticle = Article.objects.all().order_by('-id')[:5]
    tui = Article.objects.filter(tui__id=1)[:5]
    index_hot = Article.objects.all().order_by('-views')[:5]
    tag = Tag.objects.all()
    return render(request, 'index.html', locals())


# 内容页
def category_show(request, sid):
    show = Article .objects.get(id=sid)
    comments = Comment.objects.filter(article=sid)

    before = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    netx = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    hot = Article.objects.all().order_by('?')[:8]  # 内容下面的您可能感兴趣的文章，随机推荐
    show.views = show.views + 1
    show.save()
    return render(request, "show.html", locals())


# 分类页
def category_list(request, lid):
    list = Article.objects.filter(category_id=lid)
    cname = Category.objects.get(id=lid)
    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(list, 1)  # 对查询到的数据对象list进行分页，设置超过1条数据就分页
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'category_list.html', locals())


# 标签页
def tag(request, itag):
    list = Article.objects.filter(tags__name=itag)
    tname = Tag.objects.get(name=itag)
    page = request.GET.get('page')
    paginator = Paginator(list, 2)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'tags.html', locals())


# 搜索页
def search(request):
    ss = request.GET.get('search')
    list = Article.objects.filter(title__icontains=ss)
    page = request.GET.get('page')
    paginator = Paginator(list, 1)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'search.html', locals())



