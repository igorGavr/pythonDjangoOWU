from django.db import models


class CarManager(models.Manager):

    def lt_seats(self, count):
        # фільтруємо наш queryset
        return self.filter(seats__lt=count)
