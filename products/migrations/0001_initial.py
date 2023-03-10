# Generated by Django 4.1.4 on 2022-12-16 15:34

import KreditCart.views
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(default=KreditCart.views.generate_unique_object_id, max_length=24, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('price', models.PositiveIntegerField()),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('for_sale', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='StockHistory',
            fields=[
                ('id', models.CharField(default=KreditCart.views.generate_unique_object_id, max_length=24, primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField()),
                ('added_by', models.ForeignKey(limit_choices_to={'groups': 'admin'}, on_delete=django.db.models.deletion.CASCADE, related_name='added_by', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'stock_history',
                'verbose_name_plural': 'Stock History',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.CharField(default=KreditCart.views.generate_unique_object_id, max_length=24, primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'stock',
                'verbose_name_plural': 'Stocks',
            },
        ),
    ]
