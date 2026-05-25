from django.utils.decorators import method_decorator
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_extensions.cache.decorators import cache_response
from .models import Comedian, Event, Feedback
from .serializers import ComedianSerializer, EventSerializer, FeedbackSerializer


class ComedianViewSet(viewsets.ModelViewSet):
    """Представление для работы с комиками.
    Поддерживает все CRUD-операции, включая массовое создание,
    обновление и удаление. GET-запросы кешируются на 15 минут.
    Фильтрация списка возможна по GET-параметру `name` (поиск по подстроке).
    """
    serializer_class = ComedianSerializer
    queryset = Comedian.objects.all()

    def get_queryset(self):
        """Фильтрация комиков по имени."""
        qs = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name__icontains=name)
        return qs

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @cache_response(60 * 15)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """POST-создание одного или нескольких комиков."""
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """PUT-обновление одного комика или списка."""
        many = isinstance(request.data, list)
        if many:
            instances = [Comedian.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """PATCH-частичное обновление одного или нескольких комиков."""
        many = isinstance(request.data, list)
        if many:
            instances = [Comedian.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, partial=True, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """DELETE-удаление одного комика или списка через параметр ids."""
        ids = request.query_params.get('ids')
        if ids:
            ids_list = [int(pk) for pk in ids.split(',')]
            Comedian.objects.filter(pk__in=ids_list).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return super().destroy(request, *args, **kwargs)


class EventViewSet(viewsets.ModelViewSet):
    """Представление для работы с мероприятиями.
    Поддерживает все CRUD-операции, включая массовые создание, обновление,
    удаление. GET-запросы кешируются. Можно фильтровать по названию и месту.
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_queryset(self):
        """Фильтрация мероприятий по названию и месту."""
        qs = super().get_queryset()
        title = self.request.query_params.get('title')
        place = self.request.query_params.get('place')
        if title:
            qs = qs.filter(title__icontains=title)
        if place:
            qs = qs.filter(place__icontains=place)
        return qs

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @cache_response(60 * 15)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """POST-создание одного или нескольких мероприятий."""
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """PUT-обновление одного мероприятия или списка."""
        many = isinstance(request.data, list)
        if many:
            instances = [Event.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """PATCH-частичное обновление одного или нескольких мероприятий."""
        many = isinstance(request.data, list)
        if many:
            instances = [Event.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, partial=True, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """DELETE-удаление одного мероприятия или списка через параметр ids."""
        ids = request.query_params.get('ids')
        if ids:
            ids_list = [int(pk) for pk in ids.split(',')]
            Event.objects.filter(pk__in=ids_list).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return super().destroy(request, *args, **kwargs)


class FeedbackViewSet(viewsets.ModelViewSet):
    """Представление для работы с отзывами.
    Поддерживает все CRUD-операции с массовыми действиями.
    GET-запросы кешируются, фильтрация по `event_id`.
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

    def get_queryset(self):
        """Фильтрация отзывов по мероприятию (event_id)."""
        qs = super().get_queryset()
        event_id = self.request.query_params.get('event_id')
        if event_id:
            qs = qs.filter(event_id=event_id)
        return qs

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @cache_response(60 * 15)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """POST-создание одного или нескольких отзывов."""
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """PUT-обновление одного отзыва или списка."""
        many = isinstance(request.data, list)
        if many:
            instances = [Feedback.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """PATCH-частичное обновление одного или нескольких отзывов."""
        many = isinstance(request.data, list)
        if many:
            instances = [Feedback.objects.get(pk=item['id']) for item in request.data]
            serializer = self.get_serializer(instances, data=request.data, partial=True, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """DELETE-удаление одного отзыва или списка через параметр ids."""
        ids = request.query_params.get('ids')
        if ids:
            ids_list = [int(pk) for pk in ids.split(',')]
            Feedback.objects.filter(pk__in=ids_list).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return super().destroy(request, *args, **kwargs)