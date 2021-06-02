# Generated by Django 3.2.3 on 2021-06-02 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiredigital_ecom', '0021_auto_20210602_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 17, 3, 59, 67643), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 17, 3, 59, 67662), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='following',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 17, 3, 59, 67643), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='following',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 17, 3, 59, 67662), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 17, 3, 59, 67643), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.CharField(blank=True, max_length=512, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='products',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 17, 3, 59, 67662), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='productsviewed',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 17, 3, 59, 67643), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='productsviewed',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 17, 3, 59, 67662), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 17, 3, 59, 67643), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 17, 3, 59, 67662), verbose_name='Updated At'),
        ),
    ]