from django.urls import path
from .views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path, include
from .views import UserProfileUpdateView, UserDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileUpdateView.as_view(), name='user-profile-update'),
    path('profile/delete/', UserDeleteView.as_view(), name='delete-user'),
    
]