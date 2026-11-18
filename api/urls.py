from django.urls import path, include
from .views import (
    SalonListCreateView,
)

urlpatterns = [
    path('salon/create/', SalonListCreateView.as_view(), name='create_service')
]