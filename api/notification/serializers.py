from rest_framework import serializers

from .models import Notification


class NotificationSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'title', 'description', 'is_active')
