# Generated by Django 5.0.1 on 2024-08-18 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileproduct',
            old_name='course',
            new_name='product',
        ),
    ]
