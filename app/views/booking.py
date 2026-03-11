from rest_framework import views
from rest_framework.response import Response

from app.serializers import BookingSerializer
from db.models import Booking


class LCBookingView(views.APIView):
    serializer_class = BookingSerializer

    def get_object(self, request, *args, **kwargs):
        booking_id = self.request.query_params.get("booking_id")
        if booking_id:
            return Booking.objects.get(id=booking_id)
        return None

    def get_queryset(self, request, *args, **kwargs):
        qs = Booking.objects.select_related("table").all()
        name = self.request.query_params.get("client_name", None)
        phone = self.request.query_params.get("client_phone", None)
        if name and phone:
            qs = qs.filter(client_name=name, client_phone=phone)
        return qs

    def update(self, request, *args, **kwargs):
        booking = self.get_object(request, *args, **kwargs)
        return Response(self.serializer_class(booking).data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset(request)
        return Response(BookingSerializer(queryset.all(), many=True).data)

    def get(self, request, *args, **kwargs):
        booking = self.get_object(request, *args, **kwargs)
        if booking is not None:
            return Response(self.serializer_class(booking).data)
        return Response(self.serializer_class(self.get_queryset(request), many=True).data)
