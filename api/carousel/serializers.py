from rest_framework import serializers

from .models import Carousel


class CarouselSerializers(serializers.HyperlinkedModelSerializer):
    photo = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Carousel
        fields = ('id', 'title', 'photo', 'is_active', 'preference')
