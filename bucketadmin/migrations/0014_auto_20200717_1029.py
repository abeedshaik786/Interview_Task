# Generated by Django 2.2.2 on 2020-07-17 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bucketadmin', '0013_funpost_liked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funpost',
            old_name='users',
            new_name='Posted_users',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='users',
            new_name='Liked_users',
        ),
        migrations.RemoveField(
            model_name='funpost',
            name='liked',
        ),
    ]
