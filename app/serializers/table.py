from rest_framework import serializers

from db.models import Table


class TableSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Table
