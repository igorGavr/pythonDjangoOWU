from rest_framework.generics import CreateAPIView, ListCreateAPIView

from .serializers import UserSerializer
from .models import UserModel


class UserCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
