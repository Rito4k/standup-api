from django.contrib import admin
from .models import Comedian, Event, Feedback


@admin.register(Comedian)
class ComedianAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'genre', 'fee_amount', 'experience')
    search_fields = ('name', 'genre')
    list_filter = ('genre',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_time', 'place', 'address', 'created_at')
    search_fields = ('title', 'description', 'place')
    list_filter = ('date_time',)
    filter_horizontal = ('comedians',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'created_at')
    search_fields = ('text',)
    list_filter = ('event', 'created_at')