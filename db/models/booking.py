from django.db import models


class Booking(models.Model):

    table = models.ForeignKey("db.Table", on_delete=models.CASCADE)

    date = models.DateTimeField(db_index=True)

    client_name = models.CharField(max_length=255)

    client_phone = models.CharField(max_length=20)

    class Meta:
        ordering = ('date',)
        unique_together = ('table', 'date')
