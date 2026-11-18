from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Salon
from .serializers import SalonSerializer
from .permissions import SalonPermissions

class SalonListCreateView(ListCreateAPIView):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
    permission_classes = [SalonPermissions]