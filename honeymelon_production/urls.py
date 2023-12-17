"""
URL configuration for honeymelon_production project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),

    # здесь делаем только перенаправление на файл url.py приложения
    path('cart/', include("cart.urls")),#если поставить на строку ниже то корзина не будет работать
    path('', include("catalog.urls")),#LOGIN_REDIRECT_URL = 'blog-home' в settings.py (возможно переделать индексную страницу) name='index-home'
    path('orders/',include("orders.urls", namespace="orders")),
    path('catalog/', include("catalog.urls")),#, namespace="catalog"
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

