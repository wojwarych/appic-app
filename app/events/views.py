from rest_framework import mixins, viewsets
from django.shortcuts import render

from .models import Event
from .serializers import EventSerializer

# Create your views here.
class EventViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
