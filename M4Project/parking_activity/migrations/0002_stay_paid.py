# Generated by Django 5.1.1 on 2024-10-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stay',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
