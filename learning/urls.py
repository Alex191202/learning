"""
URL configuration for learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings           # <- новый импорт настроек
from django.conf.urls.static import static # <- новый импорт обработчика статики
from django.contrib.auth import views as auth_views

app_name = 'stock'  # Убедитесь, что это указано

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock/', include(('stock.urls', 'stock'), namespace='stock')),
    path('login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='stock:list'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # <- добавляем обработчик статики к списку узлов


