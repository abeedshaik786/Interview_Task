# Generated by Django 2.2.2 on 2020-07-16 11:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucketadmin', '0008_auto_20200716_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funpost',
            name='Liked_user',
            field=models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
