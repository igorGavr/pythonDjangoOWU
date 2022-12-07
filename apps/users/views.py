from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer
from .permissions import IsSuperUser


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)
    # permission_classes = (IsSuperUser,)  ----> таким чином створювати Юзерів зможе тільки superuser
