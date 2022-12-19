from django.db import models
from apps.users.models import UserModel as User
from django.contrib.auth import get_user_model

UserModel: User = get_user_model()


class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_park'
        ordering = ['id']

    name = models.CharField(max_length=10)
    # створюємо звязок один до багатьох --> тобто в кожного юзера буде кілька автопарків
    # user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks')
    # створюємо звязок багато до багатьох --> тобто в кожного юзера буде багато
    # автопарків та в автопарку буде багато юзерів
    users = models.ManyToManyField(UserModel, through='UsersAutoParksModel', related_name='auto_parks')


class UsersAutoParksModel(models.Model):
    class Meta:
        db_table = 'cars_auto_parks'


    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE)
