from rest_framework.serializers import ModelSerializer

from .models import AutoParkModel
from ..cars.serializers import CarSerializer


class AutoParkSerializer(ModelSerializer):
    # привязуємо до певного автопарку всі його машини
    cars = CarSerializer(many=True, read_only=True)
    class Meta:
        model = AutoParkModel
        fields = '__all__'
