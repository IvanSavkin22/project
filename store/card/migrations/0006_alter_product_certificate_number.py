# Generated by Django 5.0.1 on 2024-12-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0005_product_remove_payment_delivery_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='certificate_number',
            field=models.CharField(max_length=10, unique=True, verbose_name='Номер заказа'),
        ),
    ]
