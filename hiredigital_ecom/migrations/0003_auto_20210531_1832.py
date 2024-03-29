# Generated by Django 3.2.3 on 2021-05-31 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiredigital_ecom', '0002_auto_20210531_1803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['updated_at'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='assets',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 18, 32, 51, 830945), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='assets',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 18, 32, 51, 830967), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 18, 32, 51, 830945), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 18, 32, 51, 830967), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='following',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 18, 32, 51, 830945), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='following',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 18, 32, 51, 830967), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 18, 32, 51, 830945), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='products',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 18, 32, 51, 830967), verbose_name='Updated At'),
        ),
    ]
