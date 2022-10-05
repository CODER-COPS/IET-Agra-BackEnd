from rest_framework import viewsets

from .serializers import NotificationSerializers
from .models import Notification


# Create your views here.


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('id')
    serializer_class = NotificationSerializers
