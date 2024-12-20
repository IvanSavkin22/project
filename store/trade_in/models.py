from django.db import models


class Trade(models.Model):
    CATEGORY_CHOICES = [
        ('cpu', 'Процессор'),
        ('gpu', 'Видеокарта'),
        ('motherboard', 'Материнская плата'),
        ('ram', 'Оперативная память'),
        ('ssd', 'SSD'),
        ('power_supply', 'Блок питания'),
        ('monitor', 'Монитор'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def get_category_display(self):
        return dict(self.CATEGORY_CHOICES).get(self.category, self.category)


class TradeInRequest(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    selected_items = models.TextField(default='N/A')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name
