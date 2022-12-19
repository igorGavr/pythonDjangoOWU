from rest_framework.serializers import ModelSerializer

from .models import AutoParkModel
from ..cars.serializers import CarSerializer


class AutoParkSerializer(ModelSerializer):
    # прописуємо щоб при запиті на auto_parks
    # відображалися всі машини цього автопарку
    # а щоб при створенні нового автопарку не
    # додавати одразу машини то прописуємо - read_only=True
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'cars')
