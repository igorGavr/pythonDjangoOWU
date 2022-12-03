from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from apps.cars.serializers import CarSerializer
from .models import AutoParkModel
from .serializers import AutoParkSerializer
from rest_framework.response import Response
from ..cars.models import CarModel

class AutoParkListView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer

class CarListCreateView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        cars = CarModel.objects.filter(auto_park_id=pk)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        serializer = AutoParkSerializer(auto_park)
        return Response(serializer.data, status.HTTP_201_CREATED)
