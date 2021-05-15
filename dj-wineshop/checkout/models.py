from django.db import models

from cart.models import Cart

class Order(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete = models.CASCADE,
        null=True,
        blank=True,
        related_name='cart_owned'
    )
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    estate = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    order_total = models.DecimalField(
        decimal_places=1,
        max_digits=12,
        default=0.0
    )
    active = models.BooleanField(default=True)
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return self.id
