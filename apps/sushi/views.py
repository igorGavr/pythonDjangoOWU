from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from apps.users.permissions import IsSuperUser
from .models import SushiModel
from .serializers import SushiSerializer


class SushiListCreateView(ListCreateAPIView):
    queryset = SushiModel.objects.all()
    serializer_class = SushiSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return AllowAny(),
        return IsAdminUser(),


class SushiRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = SushiModel.objects.all()
    serializer_class = SushiSerializer
    permission_classes = (IsAdminUser,)
