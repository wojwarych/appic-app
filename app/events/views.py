from django.db import IntegrityError
from rest_framework import mixins, viewsets
from rest_framework.exceptions import APIException
from django.shortcuts import render
from django.db.models import Prefetch

from .models import Event, Performance
from .serializers import EventSerializer, PerformanceSerializer

# Create your views here.
class EventViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Event.objects.all().prefetch_related(
        Prefetch("performances", queryset=Performance.objects.order_by("-start"))
    )
    serializer_class = EventSerializer


class PerformanceViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Performance.objects.all().select_related("event")
    serializer_class = PerformanceSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError as exc:
            raise APIException(detail=exc)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except IntegrityError as exc:
            raise APIException(detail=exc)

    def partial_update(self, request, *args, **kwargs):
        try:
            return super().partial_update(request, *args, **kwargs)
        except IntegrityError as exc:
            raise APIException(detail=exc)
