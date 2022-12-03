from django.db import models

#Створити модель CarModel з такими полями:
# - марка машини
# - рік випуску
# - кількість місць
# - тип кузову
# - об'єм двигуна (float)
#
# реалізувати всі CRUD операції
#
# ***при виведені всіх машин показувати
# тільки (id, марку машини та рік)
class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    seats = models.IntegerField()
    body = models.CharField(max_length=20)
    engine_volume = models.FloatField()
