from rest_framework import serializers

from .models import Event, Performance


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = "__all__"

    def create(self, validated_data):
        self.is_timestamp_within_range(validated_data)
        return super().create(validated_data)

    def is_timestamp_within_range(self, validated_data):
        event = validated_data["event"]
        performance_start = validated_data["start"]
        performance_end = validated_data["end"]
        if (
            not event.start <= performance_start <= event.end
            or not event.start <= performance_end <= event.end
        ):
            raise serializers.ValidationError("Performance dates are out of range of Event!")


class EventSerializer(serializers.ModelSerializer):
    performances = PerformanceSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = "__all__"
