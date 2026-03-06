from rest_framework import serializers

from app.serializers.table import TableSerializer
from db.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    table = TableSerializer()

    class Meta:
        fields = '__all__'
        model = Booking
