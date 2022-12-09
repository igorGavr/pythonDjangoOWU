from typing import Type

from rest_framework_simplejwt.tokens import BlacklistMixin, Token

from django.contrib.auth import get_user_model

from rest_framework.generics import get_object_or_404

from apps.users.models import UserModel as User

from core.enums.action_enum import ActionEnum
from core.exceptions.jwt_exception import JWTException

UserModel: User = get_user_model()
TokenClass = Type[BlacklistMixin | Token]


class ActivateToken(BlacklistMixin, Token):
    lifetime = ActionEnum.ACTIVATE.exp_time
    token_type = ActionEnum.ACTIVATE.token_type


class JWTService:
    @staticmethod
    def create_token(user, token_class: TokenClass):
        return token_class.for_user(user)

    @staticmethod
    def validate_token(token, token_class: TokenClass):
        try:
            # передаємо токен
            token_res = token_class(token)
            # перевіряємо чи знаходиться наш токен в табл. token_blacklist
            token_res.check_blacklist()
        except (Exception,):
            raise JWTException
        # якщо наш токен ОК то передаємо його в blacklist
        token_res.blacklist()
        # відхоплюємо Айдішку
        user_id = token_res.payload.get('user_id')
        # якщо все ОК то поверне нам Юзера
        return get_object_or_404(UserModel, pk=user_id)