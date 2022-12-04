from rest_framework.generics import CreateAPIView

from .permissions import IsSuperUser
from .serializers import UserSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    #  створювати юзерів може лише super_user
    permission_classes = (IsSuperUser,)