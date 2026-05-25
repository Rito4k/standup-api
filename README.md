# standup-api
API для управления стендапом (Домашнее задание 6)

# Standup API

## Описание проекта
API для управления комиком, мероприятиями (с указанием места и адреса) и отзывами посетителей.
Проект реализован на Django REST Framework с поддержкой массовых операций, фильтрации и кеширования.

## Функционал
- Управление комиками: создание, редактирование, фильтрация по имени и жанру.
- Управление мероприятиями: указание места, адреса, даты, привязка нескольких комиков к одному событию (ManyToMany).
- Отзывы: гости могут оставлять комментарии к мероприятиям без регистрации (анонимно).
- Массовые операции: создание, обновление и удаление пачками (списком).
- Кеширование: GET-запросы детального просмотра кешируются на 15 минут.

## Эндпоинты

### Основные ресурсы

#### Комики (Comedians)
- GET /api/v1/comedians/ — список комиков (фильтрация по name, genre)
- POST /api/v1/comedians/ — создание одного или списка комиков
- GET /api/v1/comedians/{id}/ — получение комика (кешируется)
- PUT /api/v1/comedians/{id}/ — полное обновление
- PATCH /api/v1/comedians/{id}/ — частичное обновление
- DELETE /api/v1/comedians/{id}/ — удаление одного комика
- DELETE /api/v1/comedians/?ids=1,2,3 — массовое удаление

#### Мероприятия (Events)
- GET /api/v1/events/ — список мероприятий (фильтрация по title, place)
- POST /api/v1/events/ — создание мероприятия (список ID комиков в comedians_id)
- GET /api/v1/events/{id}/ — получение мероприятия с вложенными комиками
- PUT /api/v1/events/{id}/ — полное обновление
- PATCH /api/v1/events/{id}/ — частичное обновление
- DELETE /api/v1/events/{id}/ — удаление мероприятия
- DELETE /api/v1/events/?ids=1,2,3 — массовое удаление

#### Отзывы (Feedbacks)
- GET /api/v1/feedbacks/ — список отзывов (фильтрация по event_id)
- POST /api/v1/feedbacks/ — создание отзыва (требует event_id)
- GET /api/v1/feedbacks/{id}/ — получение отзыва
- PUT /api/v1/feedbacks/{id}/ — полное обновление
- PATCH /api/v1/feedbacks/{id}/ — частичное обновление
- DELETE /api/v1/feedbacks/{id}/ — удаление отзыва
- DELETE /api/v1/feedbacks/?ids=1,2,3 — массовое удаление

## Документация API
Интерактивная документация доступна по адресу:
- Swagger UI: /api/schema/swagger-ui/
- OpenAPI схема: /api/schema/

## Установка
1. Клонировать репозиторий
2. Создать виртуальное окружение: python -m venv venv
3. Активировать: venv\Scripts\activate
4. Установить зависимости: pip install -r requirements.txt
5. Применить миграции: python manage.py migrate
6. Запустить сервер: python manage.py runserver 10000

## Технологии
- Python 3.x
- Django 5.x
- Django REST Framework
- SQL Server
- drf-spectacular (Swagger)
- drf-extensions (для кеширования)

## Автор
Margo