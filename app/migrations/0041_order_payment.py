# Generated by Django 4.2.4 on 2023-09-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_category_is_sub_category_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
