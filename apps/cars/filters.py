from django_filters import rest_framework as filters

from .models import CarModel


class CarFilter(filters.FilterSet):
    year_gt = filters.NumberFilter(field_name='year', lookup_expr='gt')
    year_lt = filters.NumberFilter(field_name='year', lookup_expr='lt')
    price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    brand_start = filters.CharFilter(field_name='brand', lookup_expr='istartswith')
    brand_end = filters.CharFilter(field_name='brand', lookup_expr='iendswith')
    brand_contain = filters.CharFilter(field_name='brand', lookup_expr='icontain')

    class Meta:
        model = CarModel
        fields = ('year_gt', 'year_lt', 'price_lt', 'price_gt', 'price_gte', 'brand_end', 'brand_start', 'brand_contain')