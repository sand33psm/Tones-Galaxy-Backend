from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, ProfileSerializer
from rest_framework import viewsets, permissions
from .models import Profile

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'username': self.user.username, 'email': self.user.email})
        return data
    
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        # Accept either username or email for login
        login_id = request.data.get("username") or request.data.get("email")
        password = request.data.get("password")

        if not login_id or not password:
            return Response({"error": "Username/Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(request, username=login_id, password=password)

        if user:
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        user.delete()  # This will also delete the user profile due to the cascade delete
        return Response({"detail": "Account and profile deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        
        
class UserProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Get the user profile associated with the currently authenticated user
        return Profile.objects.get(user=self.request.user)

    def get(self, request, *args, **kwargs):
        # Retrieve and return the profile of the authenticated user
        profile = self.get_object()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        # Update the profile of the authenticated user
        profile = self.get_object()
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)