from django.db import models
from django.conf import settings
import uuid

class Ringtone(models.Model):
    GENRE_CHOICES = [
        ('pop', 'Pop'),
        ('rock', 'Rock'),
        ('hiphop', 'Hip-hop'),
        ('jazz', 'Jazz'),
        ('classical', 'Classical'),
        ('electronic', 'Electronic'),
        ('others', 'Others'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='ringtones/')
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, blank=True)
    tags = models.CharField(max_length=255, blank=True)  # Comma-separated tags
    likes = models.PositiveIntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_tags(self):
        """
        Returns a list of tags by splitting the comma-separated tags string.
        """
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
