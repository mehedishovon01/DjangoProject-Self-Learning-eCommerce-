# Generated by Django 3.0.4 on 2020-04-09 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
    ]
