from django.urls import path

from .views import CarListCreateView, CarRetrieveUpdateDestroyView, AddCarPhotoView


urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/photo', AddCarPhotoView.as_view())
]