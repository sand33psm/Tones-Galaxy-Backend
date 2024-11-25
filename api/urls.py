from django.urls import path, include

urlpatterns = [
    path('v1/users/', include('users.urls')),
    path('v1/ringtones/', include('ringtones.urls')),  # Ringtones-related endpoints

]