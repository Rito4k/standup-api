from django.db import models


class Comedian(models.Model):
    """Модель комика."""
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Event(models.Model):
    """Модель мероприятия."""
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    place = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    comedians = models.ManyToManyField(
        Comedian,
        related_name='events',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    """Модель обратной связи по мероприятию (оставляют зрители без регистрации)."""
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отзыв на {self.event.title}'