# Generated by Django 4.1.2 on 2023-01-23 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_delete_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
    ]