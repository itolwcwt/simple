from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('<int:sid>/', views.comment, name='comment'),
]
