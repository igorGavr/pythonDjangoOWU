from django_filters import rest_framework as filters

from .models import CarModel


class CarFilter(filters.FilterSet):
    year_gt = filters.NumberFilter(field_name='year', lookup_expr='gt')
    year_lt = filters.NumberFilter(field_name='year', lookup_expr='lt')
    brand_start = filters.CharFilter(field_name='brand', lookup_expr='istartswith')

    class Meta:
        model = CarModel
        fields = ('year_gt', 'year_lt', 'brand_start')