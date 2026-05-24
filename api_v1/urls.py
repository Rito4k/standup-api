from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RoleViewSet, UserViewSet, UserStatusViewSet,
    ComedianViewSet, PlaceViewSet, EventViewSet, EventStatusViewSet,
    PerformanceViewSet, PerformanceStatusViewSet,
    TicketViewSet, TicketStatusViewSet,
    FeedbackViewSet
)

router = DefaultRouter()
router.register(r'roles', RoleViewSet, basename='role')
router.register(r'users', UserViewSet, basename='user')
router.register(r'user-statuses', UserStatusViewSet, basename='userstatus')
router.register(r'comedians', ComedianViewSet, basename='comedian')
router.register(r'places', PlaceViewSet, basename='place')
router.register(r'events', EventViewSet, basename='event')
router.register(r'event-statuses', EventStatusViewSet, basename='eventstatus')
router.register(r'performances', PerformanceViewSet, basename='performance')
router.register(r'performance-statuses', PerformanceStatusViewSet, basename='performancestatus')
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'ticket-statuses', TicketStatusViewSet, basename='ticketstatus')
router.register(r'feedbacks', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('', include(router.urls)),
]