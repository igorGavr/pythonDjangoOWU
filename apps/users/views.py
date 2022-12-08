from rest_framework.generics import CreateAPIView, ListCreateAPIView, GenericAPIView, UpdateAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, AvatarSerializer
from .permissions import IsSuperUser
from rest_framework.permissions import IsAdminUser, AllowAny
from abc import ABC, abstractmethod
from apps.users.models import UserModel as User
from apps.auto_parks.serializers import AutoParkSerializer

UserModel: User = get_user_model()


class UserCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    # permission_classes = (IsSuperUser,)  ----> таким чином створювати Юзерів зможе тільки superuser


class AdminTools(GenericAPIView, ABC):
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        # всі залогінені користувачі крім мене
        return UserModel.objects.exclude(pk=self.request.user.id)

    @abstractmethod
    def patch(self, *args, **kwargs):
        pass


class SuperUserTools(AdminTools, ABC):
    permission_classes = (IsSuperUser,)


class UserActivateView(AdminTools):
    def patch(self, *args, **kwargs):
        user: User = self.get_object()

        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserDeactivateView(AdminTools):
    def patch(self, *args, **kwargs):
        user: User = self.get_object()

        if user.is_active:
            user.is_active = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserToAdminView(SuperUserTools):
    def patch(self, *args, **kwargs):
        user: User = self.get_object()

        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(SuperUserTools):
    def patch(self, *args, **kwargs):
        user: User = self.get_object()

        if user.is_staff:
            user.is_staff = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

class AutoParkListCreateView(GenericAPIView):
    def get_object(self) -> User:
        return self.request.user
    def get(self, *args, **kwargs):
        auto_parks = self.get_object().auto_parks
        serializer = AutoParkSerializer(auto_parks, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = AutoParkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = self.get_object()
        serializer.save(user=user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_201_CREATED)

class AddAvatarView(UpdateAPIView):
    serializer_class = AvatarSerializer
    http_method_names = ('patch',)

    # переоприділяємо метод який поверне мені профайл залогованого юзера,
    # і цей профайл ми будемо змінювати
    def get_object(self):
        return self.request.user.profile

