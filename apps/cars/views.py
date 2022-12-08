from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404, GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    CreateAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import CarSerializer
from .models import CarModel


############################################
#####          APIView             ####
############################################
# # GET та POST запити,
# class CarListCreateView(APIView):
#     def get(self, *args, **kwargs):
#         qs = CarModel.objects.all()
#         # qs = CarModel.objects.all().exclude(brand='KIA')
#         # qs = CarModel.objects.all()[0:2]
#         # qs = qs.filter(brand='mazda')
#         # qs = qs.filter(brand='mazda')
#         # qs = qs.filter(brand__iendswith='a').filter(year__in=[2000, 2008, 2033])
#         # qs = qs.filter(brand__iendswith='a').filter(year__range=(2000, 2008))
#         # qs = qs.order_by('brand')
#         # qs = qs.order_by('-brand', 'year')
#         # qs = qs.order_by('-brand', 'year').reverse()
#         # qs = qs.order_by('brand')
#         # print(qs.count())
#         query = self.request.query_params.dict()
#         year = query.get('lt_year')
#         if year:
#             qs = qs.filter(year__lte=year)
#         serializer = CarSerializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# # GET/pk, PUT, PATCH, DELETE
# class CarRetrieveUpdateDestroyView(APIView):
#
#     def get(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         qs = CarModel.objects.all()
#         car = get_object_or_404(qs, pk=pk)
#         serializer = CarSerializer(car)
#         return Response(serializer.data)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         data = self.request.data
#         qs = CarModel.objects.all()
#         car = get_object_or_404(qs, pk=pk)
#         serializer = CarSerializer(car, data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         data = self.request.data
#         qs = CarModel.objects.all()
#         car = get_object_or_404(qs, pk=pk)
#         serializer = CarSerializer(car, data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         exists = CarModel.objects.filter(pk=pk).exists()
#         if not exists:
#             return Response('Not found', status.HTTP_404_NOT_FOUND)
#
#         CarModel.objects.get(pk=pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ############################################
# #####          GenericAPIView             ####
# ############################################
# # GET та POST запити,
# class CarListCreateView(GenericAPIView):
#     queryset = CarModel.objects.all()
#     # для фільтрування в залежності від query_params
#     # def get_queryset(self):
#     #     query = self.request.query_params.dict()
#     #     queryset = super().get_queryset()
#     #     year = query.get('lt_year')
#     #     if year:
#     #         queryset = queryset.filter(year__lt=year)
#     #     return queryset
#
#     def get(self, *args, **kwargs):
#         serializer = CarSerializer(self.get_queryset(), many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
# # GET/pk, PUT, PATCH, DELETE
# class CarRetrieveUpdateDestroyView(GenericAPIView):
#     queryset = CarModel.objects.all()
#
#     def get(self, *args, **kwargs):
#         car = self.get_object()
#         serializer = CarSerializer(car)
#         return Response(serializer.data)
#
#     def put(self, *args, **kwargs):
#         data = self.request.data
#         car = self.get_object()
#         serializer = CarSerializer(car, data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         data = self.request.data
#         car = self.get_object()
#         serializer = CarSerializer(car, data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         self.get_object().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# ############################################
# #####          mixins                   ####
# ############################################
# # ListModelMixin - вивести всіх
# # RetrieveModelMixin - взяти по Айді
# # CreateModelMixin - створити
# # UpdateModelMixin - оновити
# # DestroyModelMixin - видалити
#
# # GET та POST запити,
# class CarListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#
# # GET/pk, PUT, PATCH, DELETE
# class CarRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

# ############################################
# #####          ListCreateAPIView           ####
# #####      RetrieveUpdateDestroyAPIView    ####
# ############################################
# # ListAPIView = GenericAPIView + ListModelMixin
# # ListCreateAPIView = GenericAPIView + ListModelMixin + CreateModelMixin
# # RetrieveUpdateDestroyAPIView = GenericAPIView + RetrieveModelMixin + UpdateModelMixin + DestroyModelMixin
#
# # GET та POST запити,
# class CarListCreateView(ListCreateAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get_queryset(self):
#         query = self.request.query_params.dict()
#         queryset = super().get_queryset()
#
#         year = query.get('lt_year')
#         if year:
#             queryset = queryset.filter(year__lt=year)
#         return queryset
#
#
# # GET/pk, PUT, PATCH, DELETE
# class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer

###########################################
####          ListAPIView             ####
####     RetrieveUpdateDestroyAPIView    ####
###########################################
# ListAPIView = запити на GET
class CarListCreateView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)

    # authentication_classes = (JWTAuthentication,)
    # IsAuthenticated - доступ тільки залогіненим юзерам
    # IsAuthenticatedOrReadOnly - записувати не має права , а читати має право
    def get_queryset(self):
        query = self.request.query_params.dict()
        # 1 variant ->
        # queryset = CarModel.objects.lt_seats(3)
        queryset = super().get_queryset()

        # 2 variant -> тут можемо звернутися до нашого методу з apps.cars.managers
        # queryset = CarModel.my_func.lt_seats(3)

        year = query.get('lt_year')
        if year:
            queryset = queryset.filter(year__lt=year)
        auto_park_id = query.get('auto_park_id')
        if auto_park_id and auto_park_id.isdigit():
            queryset = queryset.filter(auto_park_id=auto_park_id)
        # if (year := query.get('lt_year')) and year.isdigit():
        #     queryset = queryset.filter(year__lt=year)
        # if (auto_park_id := query.get('auto_park_id')) and auto_park_id.isdigit():
        #     queryset = queryset.filter(auto_park_id=auto_park_id)
        return queryset


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
