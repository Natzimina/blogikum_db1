#
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('blog.urls')),  # теперь используем blog
# ]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # подключение твоего приложения
    path('accounts/', include('django.contrib.auth.urls')),  # 👈 ВОТ ЭТА СТРОКА — ОБЯЗАТЕЛЬНА
]


