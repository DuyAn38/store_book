# Generated by Django 4.2.6 on 2023-11-13 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_remove_cart_size_remove_orderitem_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
