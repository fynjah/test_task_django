from django.db import models


class Table(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)


class Booking(models.Model):

    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True, db_index=True)

    client_name = models.CharField(max_length=255)

    client_phone = models.CharField(max_length=20)

    class Meta:
        ordering = ('date',)
