# Generated by Django 5.1.1 on 2024-12-02 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0005_userprofile_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='card_details',
        ),
        migrations.DeleteModel(
            name='CardDetails',
        ),
    ]