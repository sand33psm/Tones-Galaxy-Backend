# Generated by Django 5.1.2 on 2025-01-01 19:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ringtones', '0007_alter_ringtone_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='ringtone',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
