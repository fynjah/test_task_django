from rest_framework import serializers

from db.models import Booking


class BookingSerializer(serializers.Serializer):

    class Meta:
        fields = '__all__'
        model = Booking