from rest_framework import viewsets

from .serializers import CarouselSerializers
from .models import Carousel


# Create your views here.


class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.all().order_by('id')
    serializer_class = CarouselSerializers
