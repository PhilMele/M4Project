# Generated by Django 5.1.1 on 2024-11-06 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parking_activity', '0001_initial'),
        ('parking_management', '0001_initial'),
        ('user_management', '0004_userprofile_stripe_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterparking',
            name='parking_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parking_management.parking'),
        ),
        migrations.AddField(
            model_name='enterparking',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_management.userprofile'),
        ),
        migrations.AddField(
            model_name='leaveparking',
            name='parking_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parking_management.parking'),
        ),
        migrations.AddField(
            model_name='leaveparking',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_management.userprofile'),
        ),
        migrations.AddField(
            model_name='stay',
            name='parking_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parking_management.parking'),
        ),
        migrations.AddField(
            model_name='stay',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_management.userprofile'),
        ),
        migrations.AddField(
            model_name='leaveparking',
            name='stay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parking_activity.stay'),
        ),
        migrations.AddField(
            model_name='enterparking',
            name='stay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parking_activity.stay'),
        ),
    ]