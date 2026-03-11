from rest_framework import serializers

from app.serializers.table import TableSerializer
from db.models import Booking, Table


class BookingSerializer(serializers.ModelSerializer):
    table = TableSerializer(read_only=True)
    table_id = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all(), source="table", write_only=True
    )
    date = serializers.DateTimeField(read_only=True)
    client_name = serializers.CharField(read_only=True)
    client_phone = serializers.CharField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Booking
