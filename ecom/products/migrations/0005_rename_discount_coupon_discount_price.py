# Generated by Django 5.1.4 on 2025-01-17 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='discount',
            new_name='discount_price',
        ),
    ]
