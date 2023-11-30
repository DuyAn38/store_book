# Generated by Django 4.2.7 on 2023-11-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0045_remove_product_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
        migrations.AddField(
            model_name='product',
            name='Author',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Numberofpages',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='product',
            name='Publishingyear',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='publisher',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_sale',
            field=models.FloatField(default=0.0),
        ),
    ]
