# Generated by Django 2.0.7 on 2018-07-11 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]