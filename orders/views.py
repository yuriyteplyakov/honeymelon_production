from django.shortcuts import render
from django.core.mail import send_mail
from .models import OrderItem
from .forms import OrderCreateForm
from django.conf import settings
from cart.cart import Cart

def order_product(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
                # Очищаем корзину
                item['product'].available = False
                item['product'].save()
            cart.clear()
            message = f'Новый заказ: {order}'
            send_mail(
                   subject = 'Новый заказ',
                   message = message,
                   
                   from_email = settings.EMAIL_HOST_USER,
                   recipient_list = [settings.EMAIL_HOST_USER],
                   fail_silently=False,
               )
               # Отправка уведомления
            return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})
