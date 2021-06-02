# Generated by Django 3.2.3 on 2021-06-01 19:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hiredigital_ecom', '0019_auto_20210601_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 19, 10, 48, 754517), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 19, 10, 48, 754536), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='following',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 19, 10, 48, 754517), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='following',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 19, 10, 48, 754536), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 19, 10, 48, 754517), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='products',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 19, 10, 48, 754536), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 19, 10, 48, 754517), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 19, 10, 48, 754536), verbose_name='Updated At'),
        ),
        migrations.CreateModel(
            name='ProductsViewed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 6, 1, 19, 10, 48, 754517), verbose_name='Created At')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2021, 6, 1, 19, 10, 48, 754536), verbose_name='Updated At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('products_viewed', models.ManyToManyField(blank=True, related_name='products_viewed', to='hiredigital_ecom.Products')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_viewed_profile', to='hiredigital_ecom.userprofile')),
            ],
            options={
                'verbose_name': 'ProductViewed',
                'verbose_name_plural': 'ProductsViewed',
            },
        ),
    ]
