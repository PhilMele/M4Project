# Generated by Django 5.1.1 on 2024-11-11 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_management', '0003_parking_max_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='max_capacity',
            field=models.IntegerField(default='50', max_length=80),
        ),
    ]