from django.db import models

class Transaction(models.Model):
    name = 'api'
    hash = models.CharField(max_length=255)
    From = models.CharField(max_length=255)
    to = models.CharField(max_length=255)
    value = models.FloatField()
    