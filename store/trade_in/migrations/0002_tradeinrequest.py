# Generated by Django 5.0.1 on 2024-11-24 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_in', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeInRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=15)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]