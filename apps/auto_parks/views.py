from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView, GenericAPIView
from apps.cars.serializers import CarSerializer
from .models import AutoParkModel
from .serializers import AutoParkSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from apps.cars.models import CarModel
from core.pagination.page_pagination import PagePagination
from .filters import AutoParkFilters


class AutoParkListCreateView(ListAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer
    pagination_class = PagePagination
    filterset_class = AutoParkFilters


class CarListCreateView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return AllowAny(),
        return IsAuthenticated(),

    def get(self, *args, **kwargs):
        pk = self.get_object()
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
