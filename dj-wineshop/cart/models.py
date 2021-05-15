from decimal import Decimal as _Decimal
from django.db import models
import random

from wine.models import Wine

class CartManager(models.Manager):
    def get_cart(self, request):
        cart_id = request.session.get('cart_id', None)
        if cart_id == None:
            is_new = True
            id = Cart.objects.generate_cart()
            cart = Cart.objects.create(cart_id=id)
            request.session['cart_id'] = id
            print(is_new)
            print(request.session.get('cart_id'))
        else:
            is_new = False
            cart = Cart.objects.get(cart_id=cart_id)
            print(is_new)
            print(request.session.get('cart_id'))
        return cart

    def generate_cart(self):
        cart_id = ''
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
        length = 50
        for x in range(length):
            cart_id += chars[random.randint(0, len(chars)-1)]
        return cart_id

class Cart(models.Model):
    cart_id = models.CharField(max_length=50, null=True)
    wines = models.ManyToManyField(
        Wine,
        blank=True,
    )
    checked_out = models.BooleanField(default=False)
    total = models.DecimalField(
        default=0.0,
        max_digits=12,
        decimal_places=1
    )

    objects = CartManager()

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        default=1
    )
    wine = models.ForeignKey(
        Wine,
        on_delete=models.CASCADE
    )
    total = models.DecimalField(
        default=0.0,
        max_digits=12,
        decimal_places=1
    )
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wine.name
