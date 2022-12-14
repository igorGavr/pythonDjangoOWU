from rest_framework.serializers import ModelSerializer

from .models import PizzaModel


class PizzaSerializer(ModelSerializer):
    class Meta:
        model = PizzaModel
        fields = '__all__'