# Generated by Django 4.2.7 on 2023-12-01 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_product_count_alter_product_numberofpages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
