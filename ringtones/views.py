from rest_framework import viewsets
from .models import Ringtone
from .serializers import RingtoneSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class RingtonePagination(PageNumberPagination):
    page_size = 10

class RingtoneViewSet(viewsets.ModelViewSet):
    queryset = Ringtone.objects.all().order_by('-created_at') 
    serializer_class = RingtoneSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = RingtonePagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set the current user as the uploader

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        ringtone = self.get_object()
        file_path = ringtone.file.path

        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{ringtone.file.name}"'
        return response
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        """
        Allow authenticated users to like or dislike a ringtone.
        """
        ringtone = self.get_object()
        user = request.user

        if user.is_authenticated:
            if user in ringtone.likes.all():
                ringtone.likes.remove(user)
                message = "You have disliked the ringtone."
            else:
                ringtone.likes.add(user)
                message = "You have liked the ringtone."

            return Response({'message': message, 'total_likes': ringtone.total_likes()}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Authentication is required to like a ringtone.'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def liked_by_user(self, request):
        """
        Returns the list of ringtones liked by the authenticated user.
        """
        user = request.user
        liked_ringtones = Ringtone.objects.filter(likes=user)
        serializer = RingtoneSerializer(liked_ringtones, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def upload(self, request):
        """
        Handle ringtone upload
        """
        file = request.FILES.get('file')
        name = request.data.get('name')
        genre = request.data.get('genre')
        description = request.data.get('description')
        tags = request.data.get('tags')

        if not file:
            return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)

        if not name or not genre:
            return Response({"error": "Name and genre are required."}, status=status.HTTP_400_BAD_REQUEST)

        ringtone = Ringtone.objects.create(
            user=request.user,
            name=name,
            file=file,
            description=description,
            genre=genre,
            tags=tags
        )
        serializer = RingtoneSerializer(ringtone)
        return Response(serializer.data, status=status.HTTP_201_CREATED)