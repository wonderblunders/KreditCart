# Generated by Django 4.1.4 on 2022-12-17 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lock', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'order_lock',
                'verbose_name_plural': 'Order Lock',
            },
        ),
    ]
