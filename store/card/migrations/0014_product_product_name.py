# Generated by Django 5.0.1 on 2024-12-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0013_delete_item_remove_product_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Название товара'),
        ),
    ]
