from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Client(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='client_profile',
        verbose_name="Пользователь"
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    
    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Salon(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name

class TimeSlot(models.Model):
    client = models.ForeignKey(
        Client, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='booked_slots',
        verbose_name="Клиент"
    )
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name='slots')
    date = models.DateField(verbose_name="Дата")
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")
    
    class Meta:
        unique_together = ('salon', 'date', 'start_time')
        ordering = ['date', 'start_time']

    def __str__(self):
        status = "Занято" if self.is_booked else "Свободно"
        return f"{self.salon.name} | {self.date} {self.start_time:%H:%M} ({status})"