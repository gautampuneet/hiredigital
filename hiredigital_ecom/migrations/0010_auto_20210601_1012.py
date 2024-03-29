# Generated by Django 3.2.3 on 2021-06-01 10:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hiredigital_ecom', '0009_auto_20210531_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 6, 1, 10, 12, 7, 844648), verbose_name='Created At')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2021, 6, 1, 10, 12, 7, 844668), verbose_name='Updated At')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted')),
                ('name', models.CharField(max_length=256, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=256, null=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=32, null=True, verbose_name='Phone Number')),
            ],
            options={
                'verbose_name': 'UserProfile',
                'verbose_name_plural': 'UserProfiles',
            },
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 10, 12, 7, 844648), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 10, 12, 7, 844668), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='following',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 10, 12, 7, 844648), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='following',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 10, 12, 7, 844668), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 10, 12, 7, 844648), verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_id',
            field=models.CharField(max_length=64, null=True, verbose_name='Product Id'),
        ),
        migrations.AlterField(
            model_name='products',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 10, 12, 7, 844668), verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_user', to='hiredigital_ecom.userprofile'),
        ),
        migrations.AlterField(
            model_name='following',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='following', to='hiredigital_ecom.UserProfile'),
        ),
        migrations.AlterField(
            model_name='following',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='hiredigital_ecom.userprofile'),
        ),
        migrations.AlterField(
            model_name='products',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_user', to='hiredigital_ecom.userprofile'),
        ),
    ]
