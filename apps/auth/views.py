from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.services.jwt_service import ActivateToken, JWTService


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        # перевіряємо токен, якщо все ОК то повертається Юзер
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)