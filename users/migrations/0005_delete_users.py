# Generated by Django 4.1.2 on 2023-01-23 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
