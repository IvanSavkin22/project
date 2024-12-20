
from django.db import models


class Part(models.Model):
    CATEGORY_CHOICES = [
        ('pc', 'Для ПК'),
    ]

    PART_TYPE_CHOICES = [
        ('gpu', 'Видеокарта'),
        ('motherboard', 'Материнская плата'),
        ('cooling', 'Система охлаждения'),
        ('ram', 'Оперативная память'),
        ('cpu', 'Процессор'),
        ('psu', 'Блок питания'),
        ('hdd', 'Жесткий диск'),
        ('ssd', 'SSD'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    part_type = models.CharField(max_length=15, choices=PART_TYPE_CHOICES)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Appointment(models.Model):
    device_name = models.CharField(max_length=255)
    problem_description = models.TextField()
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class PersonalizationRequest(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
