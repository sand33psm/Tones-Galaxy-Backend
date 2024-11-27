from rest_framework import viewsets
from .models import Ringtone
from .serializers import RingtoneSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class RingtoneViewSet(viewsets.ModelViewSet):
    queryset = Ringtone.objects.all()
    serializer_class = RingtoneSerializer
    permission_classes = [IsOwnerOrReadOnly]

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
