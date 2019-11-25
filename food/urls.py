from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('', views.index, name='index'),
    path('show-<int:sid>.html', views.category_show, name='category_show'),  # 内容页
    path('list-<int:lid>.html', views.category_list, name='category_list'),  # 列表页
    path('tag/<itag>', views.tag, name='tag'),  # 标签列表页
    path('s/', views.search, name='search'),  # 搜索列表页

]
