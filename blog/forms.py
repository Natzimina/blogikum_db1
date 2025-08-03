from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Форма для создания и редактирования поста
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'is_published']

# Форма регистрации пользователя
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']