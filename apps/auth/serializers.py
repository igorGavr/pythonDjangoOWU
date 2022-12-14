from django.contrib.auth import get_user_model

from apps.users.models import UserModel as User

UserModel: User = get_user_model()

from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('password',)
