# Generated by Django 5.0.1 on 2024-11-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_subcategory_product_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='battery',
            field=models.CharField(default='N/A', max_length=255),
        ),
    ]