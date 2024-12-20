from django.db import models
from decimal import Decimal
from store.profiles.models import User
from store.product.models import Product
from store.servicer.models import Part


class Basket(models.Model):
    class Status(models.TextChoices):
        OPEN = "open", "Open"
        CLOSED = "closed", "Closed"

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="baskets", null=True, blank=True)
    status = models.CharField(choices=Status, default=Status.OPEN, max_length=20)
    created_data = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        price = Decimal('0.00')
        for line in self.basket_lines.all():
            if line.price is not None:
                price += line.price
        return price

    def get_products_ids(self):
        products_ids = []
        for line in self.basket_lines.all():
            products_ids.append(line.product.id)
        return products_ids

    def clear(self):
        self.basket_lines.all().delete()


class Line(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, null=True, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    quantity = models.PositiveIntegerField(default=1)
    created_date = models.DateField(auto_now_add=True)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket_lines')

    def __str__(self):
        return f"{self.product or self.part} in basket"
