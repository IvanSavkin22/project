from django.db import models

from store.basket.models import Basket
from store.profiles.models import User


class Order(models.Model):
    class Status(models.TextChoices):
        WAITING = "WAITING", "Waiting"
        COMPLETED = "COMPLETED", "Completed"

    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Status.choices, max_length=40, default=Status.WAITING)

    def __str__(self):
        return f"Order {self.id} - {self.user.username} - {self.status}"