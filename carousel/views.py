from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from carousel.models import Carousel
from carousel.serializers import CarouselSerializer


@api_view(['GET', 'POST'])
def carousel_list(request, format=None):
    """
    List all carousel, or create a new carousal.
    """
    if request.method == 'GET':
        carousels = Carousel.objects.all()
        serializer = CarouselSerializer(carousels, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CarouselSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def carousel_detail(request, pk, format=None):
    """
    Retrieve, update or delete a carousel.
    """
    try:
        carousel = Carousel.objects.get(pk=pk)
    except Carousel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarouselSerializer(carousel)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarouselSerializer(carousel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        carousel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
