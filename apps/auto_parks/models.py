from django.db import models
from apps.users.models import UserModel as User
from django.contrib.auth import get_user_model

UserModel: User = get_user_model()
class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_park'

    name = models.CharField(max_length=10)
    # створюємо звязок один до багатьох --> тобто в кожного юзера буде кілька автопарків
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks')