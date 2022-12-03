from rest_framework.generics import ListCreateAPIView, GenericAPIView
from apps.cars.serializers import CarSerializer
from .models import AutoParkModel
from .serializers import AutoParkSerializer
from rest_framework.response import Response

class AutoParkListView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer

class AddCarToAutoParkView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        serializer = AutoParkSerializer(auto_park)
        return Response(serializer.data)