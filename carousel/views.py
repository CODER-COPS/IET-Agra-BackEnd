from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from carousel.models import Carousel
from carousel.serializers import CarouselSerializer


@csrf_exempt
def carousel_list(request):
    """
    List all carousel, or create a new carousal.
    """
    if request.method == 'GET':
        carousels = Carousel.objects.all()
        serializer = CarouselSerializer(carousels, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CarouselSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def carousel_detail(request, pk):
    """
    Retrieve, update or delete a carousel.
    """
    try:
        carousel = Carousel.objects.get(pk=pk)
    except Carousel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CarouselSerializer(carousel)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CarouselSerializer(carousel, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        carousel.delete()
        return HttpResponse(status=204)
