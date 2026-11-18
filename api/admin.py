from django.contrib import admin
from .models import Salon, TimeSlot, Client

admin.site.register(Salon)
admin.site.register(TimeSlot)
admin.site.register(Client)