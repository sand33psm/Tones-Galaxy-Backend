from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Allow login with either username or email
        if username is None:
            username = kwargs.get('email')
        
        # Try to get the user by username or email
        try:
            user = User.objects.get(username=username) if User.objects.filter(username=username).exists() else User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        
        # Check password
        if user.check_password(password):
            return user
        return None
