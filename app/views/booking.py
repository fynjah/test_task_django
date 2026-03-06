from rest_framework import generics

from app.serializers import BookingSerializer
from db.models import Booking

class LCBookingView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        qs = Booking.objects.select_related("table").all()
        date = self.request.query_params.get("date", None)

        if date:
            qs = qs.filter(
                date__gte=date
            )
        return qs
