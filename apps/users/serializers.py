from rest_framework.serializers import ModelSerializer
from apps.auto_parks.serializers import AutoParkSerializer
from typing import Type
from django.contrib.auth import get_user_model
from apps.users.models import UserModel as User

UserModel: Type[User] = get_user_model()


class UserSerializer(ModelSerializer):
    auto_parks = AutoParkSerializer(many=True)
    class Meta:
        model = UserModel

        fields = (
            'id', 'email', 'password', 'is_staff', 'is_superuser', 'is_active',
            'created_at', 'updated_at', 'last_login', 'auto_parks'
        )
        read_only_fields = ('id', 'is_staff', 'is_superuser', 'is_active',
                            'created_at', 'updated_at', 'last_login', 'auto_parks')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user
