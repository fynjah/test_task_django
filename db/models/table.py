from django.db import models


class Table(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
