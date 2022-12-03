from django.db import models

class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_park'

    name = models.CharField(max_length=10)