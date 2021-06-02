# Generated by Django 3.2.3 on 2021-06-02 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiredigital_ecom', '0020_auto_20210601_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 12, 1, 31, 620641), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 12, 1, 31, 620662), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='following',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 12, 1, 31, 620641), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='following',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 12, 1, 31, 620662), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 12, 1, 31, 620641), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='products',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 12, 1, 31, 620662), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='productsviewed',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 12, 1, 31, 620641), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='productsviewed',
            name='products_viewed',
            field=models.ManyToManyField(blank=True, default=[], related_name='products_viewed', to='hiredigital_ecom.Products'),
        ),
        migrations.AlterField(
            model_name='productsviewed',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 12, 1, 31, 620662), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 12, 1, 31, 620641), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 12, 1, 31, 620662), verbose_name='Updated At'),
        ),
    ]
