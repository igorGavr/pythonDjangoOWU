from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.cars.serializers import CarSerializer
from .models import AutoParkModel
from .serializers import AutoParkSerializer
from rest_framework.response import Response
from ..cars.models import CarModel
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# UserModel:User = get_user_model()  # витягуємо UserModel
# UserModel.objects.filter(username__startswith='bob')  # і користуємось як рідною

class AutoParkListCreateView(ListCreateAPIView):
    # тут формується запит, тобто звичайний SELECT, запит ще не виконується
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class CarListCreateView(GenericAPIView):
    # GenericAPIView дає нам змогу винести наш queryset в зміну класу
    queryset = AutoParkModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return AllowAny(),
        return IsAuthenticated(),
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')                               # витягуємо pk автопарку
        cars = CarModel.objects.filter(auto_park_id=pk)     # фільтруємо по pk
        serializer = CarSerializer(cars, many=True)         #
        return Response(serializer.data, status.HTTP_200_OK)#

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        serializer = AutoParkSerializer(auto_park)
        return Response(serializer.data, status.HTTP_201_CREATED)
