# Generated by Django 2.2.2 on 2019-09-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0002_auto_20190924_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='driver_name',
            field=models.CharField(default='DEFAULT VALUE', max_length=100),
        ),
    ]