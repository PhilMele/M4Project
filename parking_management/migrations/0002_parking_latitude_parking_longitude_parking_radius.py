# Generated by Django 5.1.1 on 2024-10-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='latitude',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='parking',
            name='longitude',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitude'),
        ),
        migrations.AddField(
            model_name='parking',
            name='radius',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Radius'),
        ),
    ]