# Generated by Django 5.0.1 on 2024-12-17 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicer', '0006_alter_part_category_alter_part_part_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TradeInRequest',
        ),
    ]