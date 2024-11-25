from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the owner of a ringtone to edit or delete it.
    Assumes the model has a 'user' field.
    """
    def has_object_permission(self, request, view, obj):
        # Allow read-only access to all users (unauthenticated or authenticated)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow editing or deleting only if the user is the owner of the ringtone
        return obj.user == request.user
