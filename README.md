# standup-api
API для управления стендапом (Домашнее задание 6)
# Standup API

## Описание проекта
API для управления стендап-мероприятиями, комиками и билетами.

## Функционал
- Управление пользователями (роли, статусы)
- Управление комиками (жанр, опыт, портфолио)
- Управление мероприятиями (место, дата, цена билетов)
- Управление выступлениями (слоты, длительность)
- Управление билетами (покупка, статусы)
- Отзывы и рейтинги

## Эндпоинты

### Справочники
- `GET /api/v1/roles/` — список ролей
- `GET /api/v1/user-statuses/` — список статусов пользователей
- `GET /api/v1/event-statuses/` — список статусов мероприятий
- `GET /api/v1/performance-statuses/` — список статусов выступлений
- `GET /api/v1/ticket-statuses/` — список статусов билетов
- `GET /api/v1/places/` — список мест проведения

### Основные ресурсы
- `GET /api/v1/users/` — список пользователей
- `POST /api/v1/users/` — создание пользователя
- `GET /api/v1/users/{id}/` — получение пользователя
- `PATCH /api/v1/users/{id}/` — обновление пользователя
- `DELETE /api/v1/users/{id}/` — удаление пользователя

- `GET /api/v1/comedians/` — список комиков
- `POST /api/v1/comedians/` — создание комика
- `GET /api/v1/comedians/{id}/` — получение комика
- `PATCH /api/v1/comedians/{id}/` — обновление комика
- `DELETE /api/v1/comedians/{id}/` — удаление комика

- `GET /api/v1/events/` — список мероприятий (с фильтрацией)
- `POST /api/v1/events/` — создание мероприятия
- `GET /api/v1/events/{id}/` — получение мероприятия
- `PATCH /api/v1/events/{id}/` — обновление мероприятия
- `DELETE /api/v1/events/{id}/` — удаление мероприятия

- `GET /api/v1/performances/` — список выступлений
- `POST /api/v1/performances/` — создание выступления
- `GET /api/v1/performances/{id}/` — получение выступления
- `PATCH /api/v1/performances/{id}/` — обновление выступления
- `DELETE /api/v1/performances/{id}/` — удаление выступления

- `GET /api/v1/tickets/` — список билетов
- `POST /api/v1/tickets/` — покупка билета
- `GET /api/v1/tickets/{id}/` — получение билета
- `PATCH /api/v1/tickets/{id}/` — обновление билета
- `DELETE /api/v1/tickets/{id}/` — удаление билета

- `GET /api/v1/feedbacks/` — список отзывов
- `POST /api/v1/feedbacks/` — создание отзыва
- `GET /api/v1/feedbacks/{id}/` — получение отзыва
- `PATCH /api/v1/feedbacks/{id}/` — обновление отзыва
- `DELETE /api/v1/feedbacks/{id}/` — удаление отзыва

## Документация API
Интерактивная документация доступна по адресу:
- Swagger UI: `/api/schema/swagger-ui/`
- OpenAPI схема: `/api/schema/`

## Установка
1. Клонировать репозиторий
2. Создать виртуальное окружение: `python -m venv venv`
3. Активировать: `venv\Scripts\activate`
4. Установить зависимости: `pip install -r requirements.txt`
5. Применить миграции: `python manage.py migrate`
6. Запустить сервер: `python manage.py runserver`

## Технологии
- Python 3.x
- Django 5.x
- Django REST Framework
- SQL Server
- drf-spectacular (Swagger)

## Автор
Margo