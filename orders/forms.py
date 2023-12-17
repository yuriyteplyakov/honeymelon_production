from django import forms
from catalog.models import Product
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'phone_number',
                  'city']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'address': 'Адрес доставки (пункта СДЭК)',
            'phone_number': 'Номер телефона',
            'city': 'Город получения',
            }
        error_messages = {
            'first_name': {
                'required': 'Пожалуйста, введите ваше имя.',
            },
            'last_name': {
                'required': 'Пожалуйста, введите вашу фамилию.',
            },
            'email': {
                'required': 'Пожалуйста, введите ваш email.',
            },
            'address': {
                'required': 'Пожалуйста, введите адрес доставки.',
            },
            'phone_number': {
                'required': 'Пожалуйста, введите номер телефона.',
            },
            'city': {
                'required': 'Пожалуйста, введите город получения.',
            },
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = self.Meta.labels[field_name]
            field.error_messages = self.Meta.error_messages

    def save(self, commit=True):
        order = super().save(commit=False)
        if commit:
            order.save()
            order.send_email()
        return order