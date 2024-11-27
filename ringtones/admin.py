from django.contrib import admin
from .models import Ringtone

@admin.register(Ringtone)
class RingtoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'genre', 'like_count', 'date_uploaded')  # Use like_count instead of likes
    search_fields = ('name', 'tags', 'user__username', 'genre')  # Enable search by tags
    list_filter = ('genre', 'date_uploaded')
    readonly_fields = ('date_uploaded',)
    fieldsets = (
        (None, {
            'fields': ('user', 'name', 'file', 'description', 'genre', 'tags', 'date_uploaded'),
        }),
    )

    def like_count(self, obj):
        """
        Returns the total number of likes for the ringtone.
        """
        return obj.likes.count()

    like_count.short_description = 'Likes'  # Displayed as column header in admin
