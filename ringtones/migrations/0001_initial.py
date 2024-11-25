# Generated by Django 5.1.3 on 2024-11-12 23:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ringtone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='ringtones/')),
                ('description', models.TextField(blank=True)),
                ('genre', models.CharField(blank=True, choices=[('pop', 'Pop'), ('rock', 'Rock'), ('hiphop', 'Hip-hop'), ('jazz', 'Jazz'), ('classical', 'Classical'), ('electronic', 'Electronic'), ('others', 'Others')], max_length=50)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
