# Generated by Django 5.1.1 on 2024-11-12 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_management', '0004_alter_parking_max_capacity'),
        ('user_management', '0004_userprofile_stripe_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='max_capacity',
            field=models.IntegerField(default='50'),
        ),
        migrations.CreateModel(
            name='IllegalParking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_reg', models.CharField(max_length=80)),
                ('parking_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parking_management.parking')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_management.userprofile')),
            ],
        ),
    ]