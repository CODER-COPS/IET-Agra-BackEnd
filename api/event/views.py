from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import EventSerializers
from .models import Event


# Create your views here.


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializers

