from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm, RegisterForm
from django.contrib.auth import login

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    success_url = reverse_lazy('blog_home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def about_view(request):  # ✅ отдельная функция
    return render(request, 'blog/about.html')