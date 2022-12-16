from rest_framework.serializers import ModelSerializer
from typing import Type
from django.contrib.auth import get_user_model
from apps.users.models import UserModel as User

UserModel: Type[User] = get_user_model()
from .models import BasketModel


class BasketSerializer(ModelSerializer):
    class Meta:
        model = BasketModel
        fields = '__all__'


class UserSerializer(ModelSerializer):
    basket = BasketSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'is_active', 'basket', 'password', 'is_staff', 'is_superuser', 'created_at', 'updated_at',
            'last_login')
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at', 'last_login')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user
