# Generated by Django 5.0.1 on 2024-11-30 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_alter_payment_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='delivery_address',
            field=models.CharField(default='N/A', max_length=60, verbose_name='Адрес клиента'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='certificate_number',
            field=models.CharField(max_length=10, unique=True, verbose_name='Номер сертификата'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='Имя Фамилия'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Номер телефона'),
        ),
    ]