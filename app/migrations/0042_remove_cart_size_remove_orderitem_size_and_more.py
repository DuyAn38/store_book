# Generated by Django 4.2.6 on 2023-11-12 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_order_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='size',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='count39',
        ),
        migrations.RemoveField(
            model_name='product',
            name='count40',
        ),
        migrations.RemoveField(
            model_name='product',
            name='count41',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image4',
        ),
    ]
