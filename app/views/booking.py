from rest_framework import generics

from app.serializers import BookingSerializer
from db.models import Booking

class LCBookingView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.select_related("table").all()
