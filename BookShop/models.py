from django.db import models
from django.contrib.auth.models import User
from bookfinds.models import Book

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    books = models.ManyToManyField(Book, related_name='carts')

class Order(models.Model):
    PAYMENT_METHOD_CHOICES = (
        (1, 'Transfer Bank'),
        (2, 'Gopay'),
        (3, 'OVO'),
    )
    payment_method = models.IntegerField(choices=PAYMENT_METHOD_CHOICES)
    order_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
