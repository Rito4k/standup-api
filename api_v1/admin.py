from django.contrib import admin
from .models import (
    User, Role, UserStatus, Comedian, Place, 
    Event, EventStatus, Performance, PerformanceStatus,
    Ticket, TicketStatus, Feedback
)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'role_title']
    search_fields = ['role_title']


@admin.register(UserStatus)
class UserStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_title']
    search_fields = ['status_title']


@admin.register(EventStatus)
class EventStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_title']
    search_fields = ['status_title']


@admin.register(PerformanceStatus)
class PerformanceStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_title']
    search_fields = ['status_title']


@admin.register(TicketStatus)
class TicketStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_title']
    search_fields = ['status_title']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'place_name', 'address', 'capacity']
    search_fields = ['place_name', 'address']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'login', 'email']
    search_fields = ['last_name', 'first_name', 'login', 'email']


@admin.register(Comedian)
class ComedianAdmin(admin.ModelAdmin):
    list_display = ['id', 'genre', 'experience']
    search_fields = ['genre']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_name', 'date_time', 'ticket_price']
    search_fields = ['event_name']
    list_filter = ['date_time']


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'slot_order', 'duration_minutes']
    list_filter = ['id_event']


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'ticket_code', 'purchase_date']
    search_fields = ['ticket_code']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating']
    list_filter = ['rating']