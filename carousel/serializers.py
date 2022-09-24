from rest_framework import serializers
from carousel.models import Carousel

class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ['id', 'title', 'photo', 'is_active', 'preference']
