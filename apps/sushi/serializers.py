from rest_framework.serializers import ModelSerializer

from .models import SushiModel


class SushiSerializer(ModelSerializer):
    class Meta:
        model = SushiModel
        fields = '__all__'
