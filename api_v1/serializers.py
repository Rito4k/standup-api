from rest_framework import serializers
from .models import (
    User, Role, UserStatus, Comedian, Place, 
    Event, EventStatus, Performance, PerformanceStatus,
    Ticket, TicketStatus, Feedback
)


class RoleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Role."""
    class Meta:
        model = Role
        fields = ['id', 'role_title']


class UserStatusSerializer(serializers.ModelSerializer):
    """Сериализатор для модели UserStatus."""
    class Meta:
        model = UserStatus
        fields = ['id', 'status_title']


class EventStatusSerializer(serializers.ModelSerializer):
    """Сериализатор для модели EventStatus."""
    class Meta:
        model = EventStatus
        fields = ['id', 'status_title']


class PerformanceStatusSerializer(serializers.ModelSerializer):
    """Сериализатор для модели PerformanceStatus."""
    class Meta:
        model = PerformanceStatus
        fields = ['id', 'status_title']


class TicketStatusSerializer(serializers.ModelSerializer):
    """Сериализатор для модели TicketStatus."""
    class Meta:
        model = TicketStatus
        fields = ['id', 'status_title']


class PlaceSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Place."""
    class Meta:
        model = Place
        fields = ['id', 'place_name', 'address', 'capacity']


# --- Основные модели со связями ---

class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.
    При чтении возвращает полные данные о роли и статусе.
    При записи принимает только их ID.
    """
    id_role = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    id_role_display = RoleSerializer(source='id_role', read_only=True)
    
    id_status = serializers.PrimaryKeyRelatedField(
        queryset=UserStatus.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    id_status_display = UserStatusSerializer(source='id_status', read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'last_name', 'first_name', 'middle_name',
            'login', 'password', 'phone', 'email',
            'id_role', 'id_role_display', 
            'id_status', 'id_status_display'
        ]
        extra_kwargs = {'password': {'write_only': True}}


class ComedianSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Comedian.
    Связь с пользователем через ID.
    """
    id_user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    id_user_display = UserSerializer(source='id_user', read_only=True)

    class Meta:
        model = Comedian
        fields = [
            'id', 'id_user', 'id_user_display', 
            'genre', 'portfolio_url', 'fee_amount', 'experience'
        ]


class EventSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Event.
    Связи с местом, статусом и организатором через ID.
    """
    id_status_event = serializers.PrimaryKeyRelatedField(
        queryset=EventStatus.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    id_status_event_display = EventStatusSerializer(source='id_status_event', read_only=True)
    
    id_place = serializers.PrimaryKeyRelatedField(
        queryset=Place.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    id_place_display = PlaceSerializer(source='id_place', read_only=True)
    
    id_organizer = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    id_organizer_display = UserSerializer(source='id_organizer', read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 'event_name', 'date_time', 'ticket_price',
            'description', 'max_participants', 'duration_minutes',
            'id_status_event', 'id_status_event_display',
            'id_place', 'id_place_display',
            'id_organizer', 'id_organizer_display'
        ]


class PerformanceSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Performance.
    Связи с мероприятием, комиком и статусом через ID.
    """
    id_event = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        write_only=True
    )
    id_event_display = EventSerializer(source='id_event', read_only=True)
    
    id_comedian = serializers.PrimaryKeyRelatedField(
        queryset=Comedian.objects.all(),
        write_only=True
    )
    id_comedian_display = ComedianSerializer(source='id_comedian', read_only=True)
    
    id_status_perf = serializers.PrimaryKeyRelatedField(
        queryset=PerformanceStatus.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    id_status_perf_display = PerformanceStatusSerializer(source='id_status_perf', read_only=True)

    class Meta:
        model = Performance
        fields = [
            'id', 'slot_order', 'duration_minutes',
            'id_event', 'id_event_display',
            'id_comedian', 'id_comedian_display',
            'id_status_perf', 'id_status_perf_display'
        ]


class TicketSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Ticket.
    Связи с мероприятием, зрителем и статусом через ID.
    """
    id_event = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        write_only=True
    )
    id_event_display = EventSerializer(source='id_event', read_only=True)
    
    id_viewer = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    id_viewer_display = UserSerializer(source='id_viewer', read_only=True)
    
    id_status_ticket = serializers.PrimaryKeyRelatedField(
        queryset=TicketStatus.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    id_status_ticket_display = TicketStatusSerializer(source='id_status_ticket', read_only=True)

    class Meta:
        model = Ticket
        fields = [
            'id', 'ticket_code', 'purchase_date',
            'id_event', 'id_event_display',
            'id_viewer', 'id_viewer_display',
            'id_status_ticket', 'id_status_ticket_display'
        ]


class FeedbackSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Feedback.
    Связи с мероприятием и зрителем через ID.
    """
    id_event = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        write_only=True
    )
    id_event_display = EventSerializer(source='id_event', read_only=True)
    
    id_viewer = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True
    )
    id_viewer_display = UserSerializer(source='id_viewer', read_only=True)

    class Meta:
        model = Feedback
        fields = [
            'id', 'rating', 'comment',
            'id_event', 'id_event_display',
            'id_viewer', 'id_viewer_display'
        ]