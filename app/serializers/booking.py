from rest_framework import serializers

from app.serializers.table import TableSerializer
from db.models import Booking, Table


class BookingSerializer(serializers.ModelSerializer):
    table = TableSerializer(read_only=True)
    table_id = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all(), source="table", write_only=True
    )

    class Meta:
        fields = '__all__'
        model = Booking
