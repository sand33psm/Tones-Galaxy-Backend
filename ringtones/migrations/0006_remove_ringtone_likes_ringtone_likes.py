# Generated by Django 5.1.3 on 2024-11-26 17:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ringtones', '0005_remove_ringtone_tags_delete_tag_ringtone_tags'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ringtone',
            name='likes',
        ),
        migrations.AddField(
            model_name='ringtone',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_ringtones', to=settings.AUTH_USER_MODEL),
        ),
    ]
