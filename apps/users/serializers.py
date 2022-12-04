from rest_framework.serializers import ModelSerializer
from typing import Type
from django.contrib.auth import get_user_model
from apps.users.models import UserModel as User

UserModel:Type[User] = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_staff', 'is_superuser', 'is_active', 'created_at', 'updated_at', 'last_login'
        )
        # прописуємо що Юзер не має права змінювати наступні параметри
        read_only_fields = ('id', 'is_staff', 'is_superuser', 'is_active', 'created_at', 'updated_at', 'last_login')
        # вказуємо що password буде використовуватися в Серіалайзері тільки для запису
        extra_kwargs = {
            'password': {
                'write_only':True
            }
        }
    # переоприділяємо метод create
    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user