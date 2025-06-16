

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),          # Главная страница
    path('add/', views.add_post, name='add_post'),        # Страница добавления поста
    path('about/', views.about, name='about'),            # О нас
    path('posts/', views.post_list, name='post_list'),    # Список постов (по желанию)
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # Детали поста
]