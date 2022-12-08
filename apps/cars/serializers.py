from rest_framework.serializers import ModelSerializer

from apps.cars.models import CarModel, CarPhotoModel


class CarPhotoSerializer(ModelSerializer):
    class Meta:
        model = CarPhotoModel
        fields = ('photo',)

    def to_representation(self, instance: CarPhotoModel):
        return instance.photo.url


class CarSerializer(ModelSerializer):
    photos = CarPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = CarModel
        # fields = '__all__'
        exclude = ('auto_park',)
