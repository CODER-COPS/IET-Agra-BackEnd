from rest_framework import serializers

from .models import Event


class EventSerializers(serializers.HyperlinkedModelSerializer):
    photo = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Event
        fields = ('id', 'title','description','photo', 'is_active',)
