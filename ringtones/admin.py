from django.contrib import admin
from .models import Ringtone

@admin.register(Ringtone)
class RingtoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'genre', 'likes', 'date_uploaded')
    search_fields = ('name', 'tags', 'user__username', 'genre')  # Enable search by tags
    list_filter = ('genre', 'date_uploaded')
    readonly_fields = ('date_uploaded', 'likes')
    fieldsets = (
        (None, {
            'fields': ('user', 'name', 'file', 'description', 'genre', 'tags', 'date_uploaded'),
        }),
    )
