# Generated by Django 2.2.2 on 2020-07-16 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bucketadmin', '0009_auto_20200716_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funpost',
            old_name='user',
            new_name='users',
        ),
    ]
