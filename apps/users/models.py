from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core import validators as V
from apps.users.managers import UserManager
from .enums import RegEx
from .services import upload_avatar


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[
        V.RegexValidator(RegEx.PASSWORD.pattern, RegEx.PASSWORD.msg)])
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    # викликаємо свій кастомний objects
    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profiles'

    name = models.CharField(max_length=20, validators=[
        V.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    surname = models.CharField(max_length=20, validators=[
        V.RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    age = models.IntegerField(validators=[
        V.MinValueValidator(18), V.MaxValueValidator(150)])
    phone = models.CharField(max_length=10, validators=[
        V.RegexValidator(RegEx.PHONE.pattern, RegEx.PHONE.msg)])
    avatar = models.ImageField(upload_to=upload_avatar, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')


class CartModel(models.Model):
    class Meta:
        db_table = 'carts'

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='cart')
