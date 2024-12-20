from django.db import models


class Payment(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Имя Фамилия")
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
    certificate_number = models.CharField(max_length=10, unique=True, verbose_name="Номер сертификата")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма покупки")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.certificate_number}"


class Product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name="Название товара", null=True)
    full_name = models.CharField(max_length=255, verbose_name="Имя Фамилия")
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
    certificate_number = models.CharField(max_length=10, unique=True, verbose_name="Номер заказа")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма покупки")
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField(max_length=50, verbose_name="Адрес клиента")

    def __str__(self):
        return f"{self.full_name} - {self.certificate_number} - {self.product_name}"
