from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ComedianViewSet, EventViewSet, FeedbackViewSet)

router = DefaultRouter()

router.register(r'comedians', ComedianViewSet, basename='comedian')
router.register(r'events', EventViewSet, basename='event')
router.register(r'feedbacks', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('', include(router.urls)),
]