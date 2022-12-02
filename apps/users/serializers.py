# from rest_framework import serializers

from rest_framework.serializers import ModelSerializer
from .models import UserModel


# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     age = serializers.IntegerField()
#     status = serializers.BooleanField()
#
#     def update(self, instance:UserModel, validated_data: dict):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()
#         return instance
#
#     def create(self, validated_data):
#         return UserModel.objects.create(**validated_data)

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'