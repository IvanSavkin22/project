# Generated by Django 5.0.1 on 2024-12-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0007_delete_product_payment_delivery_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Имя Фамилия')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('certificate_number', models.CharField(max_length=10, unique=True, verbose_name='Номер заказа')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма покупки')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('delivery_address', models.TextField(max_length=50, verbose_name='Адрес клиента')),
            ],
        ),
        migrations.RemoveField(
            model_name='payment',
            name='delivery_address',
        ),
    ]