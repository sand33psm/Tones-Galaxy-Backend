from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

# Inline for UserProfile
class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

# Custom UserAdmin for CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']
    search_fields = ('username', 'email')
    ordering = ('username',)
    
    # Customize fieldsets to include only fields related to CustomUser
    fieldsets = UserAdmin.fieldsets

    # Add the UserProfile inline to the CustomUserAdmin
    inlines = (UserProfileInline,)

# Register the CustomUser model and the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
