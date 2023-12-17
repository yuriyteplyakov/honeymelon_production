from django.db import models
from django.core.mail import send_mail
from catalog.models import Product
from honeymelon_production.settings import EMAIL_HOST_USER


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name = 'Имя')
    last_name = models.CharField(max_length=100, verbose_name = 'Фамилия')
    email = models.EmailField()
    address = models.CharField(max_length=250, verbose_name = 'Адрес пункта выдачи СДЭК')
    phone_number = models.CharField(max_length=11, verbose_name='Номер телефона')
    city = models.CharField(max_length=100, verbose_name = 'Город получения')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
        
    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)
        
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for item in self.items.all():
            product = item.product
            product.available = False
            product.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    quantity = models.PositiveIntegerField(default=1)
 
    def __str__(self):
        return '{}'.format(self.id)
 
    def get_cost(self):
        return self.price * self.quantity
    
    def get_product_image_url(self):
        return self.product.image.url

    def get_product_name(self):
        return self.product.name