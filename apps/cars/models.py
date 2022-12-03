from django.db import models
from django.core import validators as V

from apps.auto_parks.models import AutoParkModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20, unique=True, validators=[
        V.MinLengthValidator(2), V.MaxLengthValidator(20)
    ])
    year = models.IntegerField(default=2000)
    seats = models.IntegerField()
    body = models.CharField(max_length=20, blank=True)
    engine_volume = models.FloatField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
