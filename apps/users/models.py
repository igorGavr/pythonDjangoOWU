from django.db import models

class UserModel(models.Model):
    class Meta:
        db_table = 'users'
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    status = models.BooleanField()