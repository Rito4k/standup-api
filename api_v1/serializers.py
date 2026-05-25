from rest_framework import serializers
from .models import Comedian, Event, Feedback


class ComedianSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comedian."""
    class Meta:
        model = Comedian
        fields = ['id', 'name', 'genre', 'fee_amount', 'experience']


class EventSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Event."""
    comedians = ComedianSerializer(many=True, read_only=True)
    comedians_id = serializers.PrimaryKeyRelatedField(
        queryset=Comedian.objects.all(),
        source='comedians',
        many=True,
        write_only=True,
        required=False
    )

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'date_time', 'description',
            'place', 'address',
            'comedians', 'comedians_id',
            'created_at'
        ]
        read_only_fields = ['created_at']


class FeedbackSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Feedback (как Comment в методичке).
    
    При создании требует указания id мероприятия (event_id),
    при чтении отдаёт информацию о мероприятии.
    """
    event = EventSerializer(read_only=True)
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        source='event',
        write_only=True
    )

    class Meta:
        model = Feedback
        fields = ['id', 'event', 'event_id', 'text', 'created_at']
        read_only_fields = ['created_at']