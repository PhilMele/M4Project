# Generated by Django 5.1.1 on 2024-09-26 21:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parking_activity', '0001_initial'),
        ('parking_management', '0001_initial'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='parking_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_management.parking'),
        ),
        migrations.AddField(
            model_name='fee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.userprofile'),
        ),
        migrations.AddField(
            model_name='stay',
            name='parking_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_management.parking'),
        ),
        migrations.AddField(
            model_name='stay',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.userprofile'),
        ),
    ]
