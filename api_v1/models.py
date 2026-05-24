from django.db import models

# --- Статусы ---

class UserStatus(models.Model):
    status_title = models.CharField(max_length=100)

    def __str__(self):
        return self.status_title
    
    class Meta:
        db_table = 'user_statuses'


class EventStatus(models.Model):
    status_title = models.CharField(max_length=100)

    def __str__(self):
        return self.status_title
    
    class Meta:
        db_table = 'event_statuses'


class PerformanceStatus(models.Model):
    status_title = models.CharField(max_length=100)

    def __str__(self):
        return self.status_title
    
    class Meta:
        db_table = 'performance_statuses'


class TicketStatus(models.Model):
    status_title = models.CharField(max_length=100)

    def __str__(self):
        return self.status_title
    
    class Meta:
        db_table = 'ticket_statuses'


# --- Основные таблицы ---

class Role(models.Model):
    role_title = models.CharField(max_length=100)

    def __str__(self):
        return self.role_title
    
    class Meta:
        db_table = 'role'


class Place(models.Model):
    place_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    capacity = models.IntegerField()

    def __str__(self):
        return self.place_name
    
    class Meta:
        db_table = 'place'


class User(models.Model):
    # Django сам создаст поле id (primary key)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    
    id_role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    id_status = models.ForeignKey(UserStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        db_table = 'user'


class Comedian(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    genre = models.CharField(max_length=200, blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return f"Comedian: {self.id_user.first_name if self.id_user else 'Unknown'}"
    
    class Meta:
        db_table = 'comedian'


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    max_participants = models.IntegerField()
    duration_minutes = models.IntegerField()

    # Связи
    id_status_event = models.ForeignKey(EventStatus, on_delete=models.SET_NULL, null=True)
    id_place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    id_organizer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='organized_events', null=True)

    def __str__(self):
        return self.event_name
    
    class Meta:
        db_table = 'event'


class Performance(models.Model):
    slot_order = models.IntegerField()
    duration_minutes = models.IntegerField()

    # Связи
    id_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    id_comedian = models.ForeignKey(Comedian, on_delete=models.CASCADE)
    id_status_perf = models.ForeignKey(PerformanceStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Performance at {self.id_event.event_name}"
    
    class Meta:
        db_table = 'performance'


class Ticket(models.Model):
    ticket_code = models.CharField(max_length=100, unique=True)
    purchase_date = models.DateTimeField(auto_now_add=True)

    # Связи
    id_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    id_viewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id_status_ticket = models.ForeignKey(TicketStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Ticket {self.ticket_code}"
    
    class Meta:
        db_table = 'ticket'


class Feedback(models.Model):
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    # Связи
    id_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    id_viewer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Feedback for {self.id_event.event_name}"
    
    class Meta:
        db_table = 'feedback'