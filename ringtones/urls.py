from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RingtoneViewSet
from django.conf.urls.static import static
from django.conf import settings


router = DefaultRouter()
router.register(r'', RingtoneViewSet)

urlpatterns = [
    path('', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
