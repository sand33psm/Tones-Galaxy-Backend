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
        ('instrumental', 'Instrumental'),
        ('bgm', 'Bgm'),
        ('remix', 'Remix'),
        ('slowed', 'Slowed'),
        ('lofi', 'Lofi'),
        ('indie', 'Indie'),
        ('k-pop', 'K-pop'),
        ('rnb', 'Rnb'),
        ('others', 'Others'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='ringtones/')
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, blank=True)
    tags = models.CharField(max_length=255, blank=True)  # Comma-separated tags
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_ringtones', blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_tags(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]

    def total_likes(self):
        """
        Returns the total number of likes.
        """
        return self.likes.count()
