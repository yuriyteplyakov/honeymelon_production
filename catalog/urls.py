from django.urls import path
from . import views
from catalog.views import gallery_view

app_name = 'catalog'
urlpatterns = [
    path('', views.index, name='catalog-home'),#LOGIN_REDIRECT_URL = 'blog-home' в settings.py (возможно переделать индексную страницу) name='index-home'
    path('gallery/', gallery_view, name='gallery'),
    path('catalog-list/', views.product_list, name='product_list'),
    path('product/save/', views.save_products_is_ajax, name='product-save'),
    path('catalog-list/saved-products/', views.all_save_view_products, name='all-save'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('catalog-list/order/', views.product_list_order, name='product_list_order'),
    path('<slug:category_slug>/order/', views.product_list_order, name='product_list_by_category_order'),
    
]