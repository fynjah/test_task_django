from rest_framework import serializers

from db.models import Table


class TableSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        fields = "__all__"
        model = Table
