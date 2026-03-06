import datetime

from django.utils import dateparse
from rest_framework import generics

from db.models import Table


class LTableView(generics.ListAPIView):

    def get_queryset(self):
        qs = Table.objects.all()
        date = self.request.query_params.get("date", None)

        if date:
            date_time = dateparse.parse_datetime(date)
            start_time = date_time - datetime.timedelta(hours=2)
            end_time = date_time + datetime.timedelta(hours=2)
            qs = qs.exclude(
                booking__date__range=(start_time, end_time)
            )
        return qs
