from django.contrib import admin
from .models import Order, OrderItem
from django.utils.safestring import mark_safe
"""
Мы используем ModelInline для модели OrderItem в OrderAdmin, чтобы включить ее в класс OrderAdmin.
Inline помогает нам поместить модель на страницу редактирования родительской модели.
""" 
# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    readonly_fields = ['get_product_image']

    def get_product_image(self, obj):
        if obj.product.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.product.image.url))
        else:
            return 'No Image'

    get_product_image.short_description = 'Product Image'
 
 
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address',
                    'phone_number', 'city', 'created', 'updated']
    list_filter = ['created', 'updated']
    inlines = [OrderItemInline]
 
 
admin.site.register(Order, OrderAdmin)