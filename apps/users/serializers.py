from rest_framework.serializers import ModelSerializer
from apps.auto_parks.serializers import AutoParkSerializer
from typing import Type
from django.contrib.auth import get_user_model
from apps.users.models import UserModel as User
from .models import ProfileModel
from django.db import transaction


UserModel: Type[User] = get_user_model()

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('name', 'surname', 'age', 'phone')

class UserSerializer(ModelSerializer):
    auto_parks = AutoParkSerializer(many=True, read_only=True)
    profile = ProfileSerializer()
    class Meta:
        model = UserModel

        fields = (
            'id', 'email', 'password', 'is_staff', 'is_superuser', 'is_active',
            'created_at', 'updated_at', 'last_login', 'auto_parks', 'profile'
        )
        read_only_fields = ('id', 'is_staff', 'is_superuser', 'is_active',
                            'created_at', 'updated_at', 'last_login', 'auto_parks')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    # тут відбувається зберігання юзера
    @transaction.atomic
    def create(self, validated_data:dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user


class AvatarSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('avatar',)