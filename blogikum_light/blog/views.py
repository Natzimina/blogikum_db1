from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # 🔒 Для ограничения доступа
from .forms import PostForm
from .models import Post

# О странице "О сайте"
def about(request):
    return render(request, 'blog/about.html')

# Главная страница блога
def blog_home(request):
    posts = Post.objects.all().order_by('-created_at')  # Новые посты сверху
    return render(request, 'blog/blog_home.html', {'posts': posts})

# 🔐 Добавление поста — только для авторизованных пользователей
@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # отложить сохранение
            post.author = request.user      # установить автора
            post.save()
            return redirect('home')  # возвращение на главную
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

# Список всех постов
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Детальный просмотр одного поста
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})