
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, register_view, about_view  # ✅ добавили about_view

urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('add/', PostCreateView.as_view(), name='add_post'),
    path('register/', register_view, name='register'),
    path('about/', about_view, name='about'),  # ✅ новый маршрут
]
