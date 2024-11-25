from rest_framework import viewsets
from .models import Ringtone
from .serializers import RingtoneSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from django.http import FileResponse


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
