from django.db import models
from django.core import validators as V


class SushiModel(models.Model):
    class Meta:
        db_table = 'sushi'

    imageUrl = models.CharField(max_length=120, unique=True, validators=[
        V.MaxLengthValidator(2), V.MaxLengthValidator(120)
    ])
    name = models.CharField(max_length=35, unique=True, validators=[
        V.MaxLengthValidator(2), V.MaxLengthValidator(35)
    ])
    weight = models.IntegerField()
    price = models.IntegerField()
    # 0-6
    category = models.IntegerField()
    rating = models.IntegerField()
    ingredients = models.CharField(max_length=150, validators=[
        V.MinLengthValidator(10), V.MaxLengthValidator(150)
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
