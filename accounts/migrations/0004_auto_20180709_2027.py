# Generated by Django 2.0.7 on 2018-07-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180709_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatars/1.png', upload_to='avatars/123/123'),
        ),
    ]