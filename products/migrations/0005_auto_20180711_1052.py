# Generated by Django 2.0.7 on 2018-07-10 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180708_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='url',
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(default='Active', max_length=30),
        ),
    ]