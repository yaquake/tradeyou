# Generated by Django 2.0.7 on 2018-07-13 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20180713_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
