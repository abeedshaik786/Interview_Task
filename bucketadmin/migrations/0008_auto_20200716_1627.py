# Generated by Django 2.2.2 on 2020-07-16 10:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bucketadmin', '0007_auto_20200716_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='funpost',
            name='Liked_user',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='funpost',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
