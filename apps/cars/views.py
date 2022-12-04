from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import CarSerializer
from .models import CarModel
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
class CarListCreateView(ListAPIView):
    # тут формується запит, тобто звичайний SELECT, запит ще не виконується
    queryset = CarModel.objects.all()
    # тут під капотом виконується запит або на створення або на отримання всіх машин,
    # валідація даних та вивід
    serializer_class = CarSerializer
    # authentication_classes = (JWTAuthentication,)
    # # дозволяємо робити запити тільки залогіненим юзерам
    # permission_classes = (IsAuthenticated,)
    # дозволяємо робити запити всім юзерам
    # permission_classes = (AllowAny,)


    def get_queryset(self):
        # витягуємо query параметри та конвертуємо їх в словник
        query = self.request.query_params.dict()
        queryset = super().get_queryset()
        # робимо перевірку - якщо в query є lt_year і воно є числом то
        # фільтруємо наш queryset - залишаться лише машинки з роком < year
        if (year := query.get('lt_year')) and year.isdigit():
            queryset = queryset.filter(year__lt=year)
        # робимо перевірку - якщо в query є auto_park_id і воно є числом то
        # фільтруємо наш queryset - залишаться лише машинки з певного автопарку
        if (auto_park_id := query.get('auto_park_id')) and auto_park_id.isdigit():
            queryset = queryset.filter(auto_park_id=auto_park_id)
        return queryset


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # тут формується запит, тобто звичайний SELECT, запит ще не виконується
    queryset = CarModel.objects.all()
    # тут під капотом виконується запит на put, patch та delete за Айдішкою,
    # валідація даних та вивід
    serializer_class = CarSerializer
