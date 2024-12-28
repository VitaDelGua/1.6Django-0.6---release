from django.db import models

class CalculateHistory(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    result = models.IntegerField()
    created_at = models.DateTimeField()
