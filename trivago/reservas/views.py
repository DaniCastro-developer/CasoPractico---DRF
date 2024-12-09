from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import RoomSerializer, ReservationSerializer
from .models import Room, Reservation

# Create your views here.
class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer