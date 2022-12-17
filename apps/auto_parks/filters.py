from .models import AutoParkModel
from django_filters import rest_framework as filters


class AutoParkFilters(filters.FilterSet):
    car_year_lt = filters.NumberFilter(field_name='cars__year', lookup_expr='lt')

    class Meta:
        model = AutoParkModel
        fields = ('car_year_lt',)
